# Vesteda Login Crawler Specification

## Base URLs
- Login page: https://hurenbij.vesteda.com/login/
- Post-login portal: Mijn Vesteda

## Authentication Flow
1. Navigate to login page
2. Input fields:
   - Email field
   - Password field
3. Submit button: "Inloggen"

## Technical Requirements
- Uses browser session management
- Requires persistent cookies
- Language options: NL/EN

## Rate Limiting & Ethics
- Implement polite crawling (delays between requests)
- Store credentials securely in .env
