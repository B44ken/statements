# Ajax (Ontario) – Notes

## Status

⚠️ **BLOCKER**: Unable to access external websites to download financial statements.

## Attempted Approaches

1. **Direct website access** - Attempted to access ajax.ca and www.ajax.ca
   - DNS resolution failed: "No address associated with hostname"
   - Network appears to be restricted in the sandboxed environment

2. **Search engines** - Attempted Google and DuckDuckGo
   - Blocked by ERR_BLOCKED_BY_CLIENT

3. **Internet Archive** - Attempted archive.org
   - DNS resolution failed

4. **Open Data Portals** - Attempted data.ontario.ca
   - Blocked by ERR_BLOCKED_BY_CLIENT

## Expected Sources

Based on typical Ontario municipality patterns, Ajax financial statements should be available at:
- Town of Ajax official website (www.ajax.ca or ajax.ca)
- Annual Financial Reports section
- Budget and Finance pages

## Next Steps Required

To complete this task, manual intervention is needed:
1. Access ajax.ca from a non-restricted environment
2. Navigate to financial reports/annual reports section
3. Download PDFs for available years (typically last 3-5 years)
4. Place files in year-based subfolders (e.g., 2024/, 2023/, etc.)

## Typical File Organization

Based on the Toronto example:
- Each year should have its own subfolder (e.g., 2024/, 2023/, 2022/)
- Files should be named descriptively (e.g., FinancialReport.pdf, AnnualReport.pdf)
- Update this notes.md with:
  - Direct links to sources
  - Any special notes about file formats or availability
  - Years covered

## Manual Download Instructions

Someone with unrestricted internet access should:
1. Go to https://www.ajax.ca (or http://www.ajax.ca if HTTPS is not available)
2. Search for "financial statements" or "annual reports"
3. Download available reports (check multiple years if available)
4. Organize into year subfolders in this directory
5. Update this notes.md with source URLs
