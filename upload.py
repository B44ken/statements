#!/usr/bin/env python3
import os
import sys
import csv
import json
import urllib.request
import urllib.error
import mimetypes

# --- Configuration ---
CSV_FILENAME = 'municipalities_clean.csv'
DEFAULT_API_URL = 'https://hub.buildcanada.com'

# --- Grug Helpers ---

def load_id_mapping(csv_path):
    """
    Reads the CSV and returns a dict: {'CityName': 'RegionID'}
    """
    mapping = {}
    if not os.path.exists(csv_path):
        print(f"ERROR: Mapping file not found: {csv_path}")
        sys.exit(1)

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Handle potential duplicates or bad data by just taking the first one
            name = row.get('name', '').strip()
            region_id = row.get('region', '').strip()
            if name and region_id:
                # If duplicates exist (e.g. 2 'Victoria's), this keeps the last one found. 
                # Ideally, we'd check Province too, but keeping it simple for now.
                mapping[name] = region_id
    
    print(f"INFO: Loaded {len(mapping)} municipality mappings.")
    return mapping

def upload_file(file_path, csd_id, year, api_key, api_url):
    """
    Uploads a single file using standard urllib (no pip install requests needed).
    """
    url = f"{api_url}/api/v1/bodies/{csd_id}/{year}"
    filename = os.path.basename(file_path)
    boundary = '----WebKitFormBoundaryGrugDev'
    
    # Build multipart form data manually
    data = []
    data.append(f'--{boundary}')
    data.append(f'Content-Disposition: form-data; name="document"; filename="{filename}"')
    data.append('Content-Type: application/pdf')
    data.append('')
    
    try:
        with open(file_path, 'rb') as f:
            data.append(f.read())
    except Exception as e:
        print(f"ERROR: Could not read file {filename}: {e}")
        return False

    data.append(f'--{boundary}--')
    data.append('')

    # Combine text headers and binary body
    body = b''
    for item in data:
        if isinstance(item, str):
            body += item.encode('utf-8') + b'\r\n'
        else:
            body += item + b'\r\n'

    req = urllib.request.Request(url, data=body)
    req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
    req.add_header('Authorization', f'Bearer {api_key}')
    req.add_header('User-Agent', 'GrugUploader/1.0')

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                print(f"SUCCESS: Uploaded {filename} (ID: {csd_id}, Year: {year})")
                return True
            else:
                print(f"INFO: Unexpected status {response.status} for {filename}")
                return False
    except urllib.error.HTTPError as e:
        resp_body = e.read().decode('utf-8')
        if e.code == 409:
            print(f"WARNING: Exists already {year} for {csd_id} (Skipping)")
            return True # Count as success/skip
        print(f"ERROR: HTTP {e.code} for {filename}: {resp_body}")
        return False
    except urllib.error.URLError as e:
        print(f"ERROR: Connection failed: {e.reason}")
        return False

# --- Main Logic ---

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <directory> <api_key> [api_url]")
        sys.exit(1)

    root_dir = sys.argv[1]
    api_key = sys.argv[2]
    api_url = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_API_URL
    
    # Locate CSV in the same folder as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, CSV_FILENAME)
    
    # 1. Load Map
    name_to_id = load_id_mapping(csv_path)

    stats = {'found': 0, 'uploaded': 0, 'failed': 0, 'skipped': 0}

    print(f"INFO: Scanning {root_dir}...")

    # 2. Walk Directory
    for current_root, dirs, files in os.walk(root_dir):
        for filename in files:
            if not filename.lower().endswith('.pdf'):
                continue
            
            file_path = os.path.join(current_root, filename)
            stats['found'] += 1

            # Structure: .../City/Year/file.pdf
            # current_root is .../City/Year
            
            year_folder = os.path.basename(current_root)
            parent_folder = os.path.dirname(current_root)
            city_name = os.path.basename(parent_folder)

            # Validate Year (simple 4 digit check)
            if not (len(year_folder) == 4 and year_folder.isdigit()):
                # This might be just a random PDF in the root or wrong folder
                continue

            # Validate City ID
            city_id = name_to_id.get(city_name)
            
            if not city_id:
                print(f"WARNING: No ID found for city '{city_name}' (Path: {file_path})")
                stats['skipped'] += 1
                continue

            # 3. Upload
            if upload_file(file_path, city_id, year_folder, api_key, api_url):
                stats['uploaded'] += 1
            else:
                stats['failed'] += 1

    # Summary
    print("\n" + "="*30)
    print("SUMMARY")
    print("="*30)
    print(f"Files Found:    {stats['found']}")
    print(f"Uploaded/Skip:  {stats['uploaded']}")
    print(f"Failed:         {stats['failed']}")
    print(f"ID Missing:     {stats['skipped']}")
    print("="*30)

    if stats['failed'] > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()