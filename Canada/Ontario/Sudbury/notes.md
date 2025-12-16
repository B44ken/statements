# Sudbury (Ontario) – Notes

## Status

Currently unable to retrieve financial statements due to network access restrictions.

## Blockers

Attempted to access the City of Greater Sudbury's financial statements but encountered the following blockers:

1. **Search engines blocked**: Google and DuckDuckGo are not accessible from the sandboxed environment
2. **Municipality website blocked**: 
   - `www.greatersudbury.ca` - DNS resolution refused
   - Unable to access the official City of Greater Sudbury website
3. **Archive services blocked**: Internet Archive (web.archive.org) is not accessible
4. **DNS restrictions**: DNS lookups for `greatersudbury.ca` domain are being refused

## Expected Sources

Based on typical municipal financial statement locations, the following URLs would likely contain the financial statements:

- City of Greater Sudbury Budget and Finance page: `https://www.greatersudbury.ca/city-hall/budget-and-finance/`
- Annual Financial Reports/Consolidated Financial Statements

## Recommended Next Steps

To complete this task, the following options are available:

1. **Manual download**: Someone with unrestricted internet access should:
   - Visit the City of Greater Sudbury official website
   - Navigate to the Budget and Finance or Financial Reports section
   - Download annual financial reports/consolidated financial statements for available years (ideally 2022, 2023, 2024)
   - Place them in year-specific subfolders (e.g., `2022/`, `2023/`, `2024/`)

2. **Alternative access method**: Whitelist the `greatersudbury.ca` domain in the sandboxed environment

## Municipality Information

- **Official Name**: City of Greater Sudbury
- **Province**: Ontario
- **Type**: City (Regional Municipality)
