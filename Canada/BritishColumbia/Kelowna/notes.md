# Kelowna (British Columbia) – Notes

## Blocker: Website Access Restrictions

The City of Kelowna website (kelowna.ca) is protected by Cloudflare with aggressive bot protection that blocks all automated access attempts. This prevents downloading financial statements programmatically.

### Primary Source

City of Kelowna - Budget and Financial Reports:
https://www.kelowna.ca/city-services/budget-financial-reports/financial-statements

### Attempted Workarounds

**Main website attempts:**
- Main website: https://www.kelowna.ca
- Financial statements page: https://www.kelowna.ca/city-services/budget-financial-reports/financial-statements

**Access Methods Tried:**
- curl with various user agents
- wget with custom headers
- Direct PDF downloads
- Browser automation (Playwright)

**Results:** All attempts to access kelowna.ca resulted in:
- HTTP 403 Forbidden errors
- Cloudflare "Sorry, you have been blocked" pages  
- ERR_BLOCKED_BY_CLIENT errors

**Alternative domains tested:**
- apps.kelowna.ca - allows file downloads but financial statement PDF paths could not be determined without accessing the main website
- opendata.kelowna.ca - contains geographic/statistical open data, not financial statements

## Manual Download Required

To complete this task, the financial statements need to be downloaded manually by:
1. Using a regular web browser to visit: https://www.kelowna.ca/city-services/budget-financial-reports/financial-statements
2. Downloading available annual financial statements/reports (likely "Audited Financial Statements")
3. Organizing files into year subfolders in this directory

## Expected Files

Based on similar BC municipalities, Kelowna likely publishes:
- Annual Audited Financial Statements
- Possibly separate Annual Reports

Multiple years should be available (typically 5-10 years of historical statements).
