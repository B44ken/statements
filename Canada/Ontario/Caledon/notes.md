# Caledon (Ontario) – Notes

## Status

**Blocker**: Unable to download financial statements due to network access restrictions in the automation environment.

## Search Attempts

Attempted to search for "Caledon financial statements" and "Caledon annual reports" but encountered the following blockers:
- Search engines (Google, DuckDuckGo) are blocked in this environment
- Direct website access to www.caledon.ca is restricted
- curl/wget attempts to access Caledon municipal website returned empty responses
- DNS resolution fails for caledon.ca and peelregion.ca domains
- Network connectivity is severely restricted in the automation environment

**This task requires manual completion with direct internet access.**

## Likely Sources

Based on typical Ontario municipal website structures, the financial statements for the Town of Caledon are likely available at:

1. **Town of Caledon Official Website**
   - Main site: https://www.caledon.ca
   - Likely path: https://www.caledon.ca/en/town-hall/financial-reports.aspx
   - Alternative: https://www.caledon.ca/en/town-hall/budget-and-finance.aspx
   
   **Note**: These URLs are speculative and untested due to network restrictions. Please verify the actual website structure during manual download, as municipal websites may have different layouts.

2. **Search Terms to Try**
   - "Town of Caledon financial statements"
   - "Caledon annual financial report"
   - "Caledon consolidated financial statements"
   - "Caledon annual report"

## Next Steps for Manual Download

1. Visit the Town of Caledon website
2. Navigate to Town Hall > Financial Reports or Budget & Finance section
3. Download financial statements/annual reports for all available years (recent years such as 2022, 2023, 2024, or older years if available)
4. Create year subfolders (e.g., 2022/, 2023/, 2024/) for each year downloaded
5. Save PDFs with consistent naming (e.g., FinancialReport.pdf or AnnualReport.pdf)
6. Update this notes.md with actual sources and links

## Notes

- Caledon is a municipality in the Regional Municipality of Peel, Ontario
- As a municipality, they are required to publish annual financial statements
- Financial statements are typically published as PDFs in the municipality's website
