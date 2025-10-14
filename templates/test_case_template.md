# Module: [Module Name]
# Version: [Version Number]
# Created By: Mohammad Tabreze
# Date: [Date]

| Test Case ID | Test Scenario | Preconditions | Test Steps | Expected Result | Priority | Type |
|---------------|---------------|----------------|-------------|------------------|-----------|------|
| TC_001 | Verify login with valid credentials | User should have valid account | 1. Open Login Page <br> 2. Enter valid credentials <br> 3. Click Login | User should be navigated to Dashboard | P1 | Functional |
| TC_002 | Validate mandatory field for Username | Login page loaded | Leave Username empty and click Login | Error “Username is required” should appear | P1 | Field Validation |
| TC_003 | Validate max character length for Password | Login page loaded | Enter more than 20 characters in password field | Error “Password too long” should appear | P2 | Edge |
