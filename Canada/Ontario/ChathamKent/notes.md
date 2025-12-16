# ChathamKent (Ontario) – Notes

## Status

**BLOCKED** - Unable to download financial statements due to network restrictions in the automated environment.

## Blockers

### Network Access Issues
The Municipality of Chatham-Kent website cannot be accessed from the current environment:

**Attempted URLs:**
- `https://chatham-kent.ca` - DNS resolution failed
- `https://www.chatham-kent.ca` - DNS resolution failed  
- `https://chathamkent.ca` - DNS resolution failed
- `https://www.ckontario.ca` - DNS resolution failed
- `https://www.chatham-kent.on.ca` - DNS resolution failed
- `https://chatham-kent.civicweb.net` - No response

**Error Details:**
- Browser: `ERR_BLOCKED_BY_CLIENT` 
- DNS: `No address associated with hostname`
- Ping: Failed to resolve hostname

### Root Cause
Network restrictions in the automated environment prevent:
- DNS resolution of ChathamKent municipality domains
- Browser access to search engines and municipality websites
- Direct HTTP/HTTPS requests to common domain patterns

## Expected Resources

Based on patterns from other Ontario municipalities (Toronto, Windsor), ChathamKent should provide:
- Annual Financial Reports (consolidated statements)
- Multiple years of historical data
- Typically available in PDF format
- Usually organized by fiscal year

## Required Manual Steps

1. **Identify correct website URL** - The Municipality of Chatham-Kent official website needs to be accessed from an unrestricted environment
2. **Locate financial documents** - Search for "Budget", "Finance", "Financial Statements", or "Annual Report" sections
3. **Download statements** - Collect PDFs for as many years as available
4. **Organize files** - Place in year subfolders following the repository pattern (e.g., `2024/`, `2023/`, etc.)
5. **Update this file** - Add source URLs and document what was found

## Recommended Next Steps

- Access from environment with unrestricted internet access
- Search: "Municipality of Chatham-Kent financial statements"
- Alternative: "Chatham-Kent annual report"
- Check Ontario municipal databases if direct website is unavailable
