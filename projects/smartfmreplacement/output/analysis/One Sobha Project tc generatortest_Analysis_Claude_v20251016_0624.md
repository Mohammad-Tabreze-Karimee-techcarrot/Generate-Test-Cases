# Requirements Analysis by Claude AI

**Project:** smartfmreplacement
**Module:** One Sobha Project tc generatortest
**Analyzed:** 2025-10-16 06:24:20

---

# STRUCTURED TEST SPECIFICATION EXTRACT

## 1. FUNCTIONAL REQUIREMENTS

### UC-125: View MIP/MOP Template
- **FR-125.1**: Super Admin and Community Admin can view MIP/MOP templates (read-only)
- **FR-125.2**: Templates managed from backend only
- **FR-125.3**: One active template per unique property combination (Master Community/Community/Tower)
- **FR-125.4**: Transaction history logging required
- **FR-125.5**: Standard search functionality

### UC-126: Master Data Setup - Welcome Pack
- **FR-126.1**: Super Admin and Community Admin can configure Welcome Pack
- **FR-126.2**: One active Welcome Pack per unique property combination
- **FR-126.3**: CRUD operations with history logging
- **FR-126.4**: Standard search functionality

### UC-127: Master Data Setup - Email Recipients
- **FR-127.1**: Super Admin only can configure email recipients
- **FR-127.2**: Multiple email recipients per community (comma-separated)
- **FR-127.3**: One active configuration per unique property combination
- **FR-127.4**: Separate MIP and MOP email recipient fields

### UC-128: Move-in Process
**Move-in Types:**
- **Owner**: 3 steps (Property Details → Verify Details → Move-in Details)
- **Tenant**: 4 steps (Property Details → Verify Details → Move-in Details → Attach Documents)
- **HHO Unit**: 2 steps (Move-in Details → Attach Document)
- **HHO Company**: 4 steps (Property Details → Verify Details → Move-in Details → Attach Documents)

**Request Statuses:**
- New
- RFI Submitted
- Approved
- Closed
- Cancelled

**Admin Actions:**
- View, Edit, Cancel, Mark RFI, Approve, Close Request

### Move-out Process
- **FR-MO.1**: Move-out request creation from closed move-in
- **FR-MO.2**: Move-out enabled 30 days before tenancy end date
- **FR-MO.3**: Statuses: New, Approved, Moved-Out, Cancelled

### Account Renewal Process
**Renewal Types:**
- **Tenant**: Requires Ejari document
- **HHO Unit**: Requires Dubai Tourism Unit Permit
- **HHO Company**: Requires DTCM, Emirates ID, Trade License

**Statuses:** New, RFI Submitted, Renewed, Cancelled

### Active Residents
- **FR-AR.1**: View resident details by type (Owner/Tenant/HHO Unit/HHO Company)
- **FR-AR.2**: View residency history (Move-in + Account Renewals)
- **FR-AR.3**: View associated assets (Access Cards, Parking)

---

## 2. UI COMPONENTS & FLOWS

### Input Fields Table - Move-in (Tenant)

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must select from list | - |
| Community | Dropdown | Y | Must select from list | - |
| Building/Street | Dropdown | Y | Must select from list | - |
| Unit Number | Text | Y | Alphanumeric | - |
| Email ID | Email | Y | Valid email format | - |
| First Name | Text | Y | Alphabetic only | - |
| Middle Name | Text | N | Alphabetic only | - |
| Last Name | Text | Y | Alphabetic only | - |
| Mobile Number | Text | Y | Format: 0555 0898XX | - |
| Emirates ID Number | Text | Y | Format: 784-xxxx-xxxxxxx-x | - |
| Emirates ID Expiry Date | Date | Y | DD/MM/YYYY, Future date | - |
| Move-in Date | Date | Y | DD/MM/YYYY | - |
| Tenancy Contract Number | Text | Y | Alphanumeric | - |
| Tenancy Contract Start Date | Date | Y | DD/MM/YYYY | - |
| Tenancy Contract End Date | Date | Y | DD/MM/YYYY, After start date | - |
| Adult(s) (Above 12 years) | Number | Y | Min: 1, Integer | 1 |
| Children (Ages 0-12) | Number | Y | Min: 0, Integer | 1 |
| Household staff(s) | Radio | Y | Yes/No | No |
| Pets(s) | Radio | Y | Yes/No | No |
| People of determination | Radio | Y | Yes/No | No |
| Please Provide Details | Textarea | N | Max length TBD | - |
| Emirates ID Front | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |
| Emirates ID Back | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |
| Ejari | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |

### Input Fields Table - Move-in (Owner)

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must select from list | - |
| Community | Dropdown | Y | Must select from list | - |
| Building/Street | Dropdown | Y | Must select from list | - |
| Unit Number | Text | Y | Alphanumeric | - |
| Move-in Date | Date | Y | DD/MM/YYYY | - |
| First Name | Text | Y | Alphabetic only | - |
| Middle Name | Text | N | Alphabetic only | - |
| Last Name | Text | Y | Alphabetic only | - |
| Mobile Number | Text | Y | Format: 0555 0898XX | - |
| Email ID | Email | Y | Valid email format | - |
| Adult(s) (Above 12 years) | Number | Y | Min: 1, Integer | 1 |
| Children (Ages 0-12) | Number | Y | Min: 0, Integer | 1 |
| Household staff(s) | Radio | Y | Yes/No | No |
| Pets(s) | Radio | Y | Yes/No | No |
| People of determination | Radio | Y | Yes/No | No |
| Please Provide Details | Textarea | N | Max length TBD | - |

### Input Fields Table - Move-in (HHO Unit)

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must select from list | - |
| Community | Dropdown | Y | Must select from list | - |
| Building/Street | Dropdown | Y | Must select from list | - |
| Unit Number | Text | Y | Alphanumeric | - |
| Move-in Date | Date | Y | DD/MM/YYYY | - |
| First Name | Text | Y | Alphabetic only | - |
| Middle Name | Text | N | Alphabetic only | - |
| Last Name | Text | Y | Alphabetic only | - |
| Mobile Number | Text | Y | Format: 0555 0898XX | - |
| Email ID | Email | Y | Valid email format | - |
| Unit Permit Number | Text | Y | Format: AB-12345678 | - |
| Unit Permit Start Date | Date | Y | DD/MM/YYYY | - |
| Unit Permit End Date | Date | Y | DD/MM/YYYY, After start date | - |
| Unit Permit | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |

### Input Fields Table - Move-in (HHO Company)

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must select from list | - |
| Community | Dropdown | Y | Must select from list | - |
| Tower/Street | Dropdown | Y | Must select from list | - |
| Unit Number | Text | Y | Alphanumeric | - |
| Move-in Date | Date | Y | DD/MM/YYYY | - |
| Email ID | Email | Y | Valid email format | - |
| First Name | Text | Y | Alphabetic only | - |
| Middle Name | Text | N | Alphabetic only | - |
| Last Name | Text | Y | Alphabetic only | - |
| Mobile Number | Text | Y | Format: 0555 0898XX | - |
| Representative Name | Text | Y | Alphabetic only | - |
| Company | Text | Y | Alphanumeric | - |
| Company Email ID | Email | Y | Valid email format | - |
| Operator Office Number | Text | Y | Format: +971 122345678 | - |
| Trade License Number | Text | Y | Numeric, 8 digits | - |
| Trade License Expiry Date | Date | Y | DD/MM/YYYY, Future date | - |
| Lease Start Date | Date | Y | DD/MM/YYYY | - |
| Lease End Date | Date | Y | DD/MM/YYYY, After start date | - |
| Nationality | Dropdown | Y | Must select from list | - |
| Emirates ID Number | Text | Y | Numeric, 8 digits | - |
| Emirates ID Expiry Date | Date | Y | DD/MM/YYYY, Future date | - |
| Unit Permit Number | Text | Y | Format: AB-12345678 | - |
| Unit Permit Start Date | Date | Y | DD/MM/YYYY | - |
| Unit Permit End Date | Date | Y | DD/MM/YYYY, After start date | - |
| Unit Permit | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |
| Emirates ID Front | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |
| Emirates ID Back | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |
| Company Trade License | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |

### Input Fields Table - Move-out

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Move-out Date | Date | Y | DD/MM/YYYY | - |
| Reason for Move-Out | Dropdown | Y | Job Relocation, etc. | - |
| Actual Move-out Date | Date | Y | DD/MM/YYYY | - |
| Acknowledgement Checkbox | Checkbox | Y | Must check | Unchecked |

### Input Fields Table - Account Renewal (Tenant)

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Tenancy Start Date | Date | Y | DD/MM/YYYY | - |
| Tenancy End Date | Date | Y | DD/MM/YYYY, After start date | - |
| Adult(s) (Above 12 years) | Number | Y | Min: 1, Integer | 1 |
| Children (Ages 0-12) | Number | Y | Min: 0, Integer | 1 |
| Household staff(s) | Radio | Y | Yes/No | No |
| Pets(s) | Radio | Y | Yes/No | No |
| People of determination | Radio | Y | Yes/No | No |
| Please Provide Details | Textarea | N | Max length TBD | - |
| Ejari | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |

### Input Fields Table - Account Renewal (HHO Unit)

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Tenancy Start Date | Date | Y | DD/MM/YYYY | - |
| Tenancy End Date | Date | Y | DD/MM/YYYY, After start date | - |
| Dubai Tourism Unit Permit | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |

### Input Fields Table - Account Renewal (HHO Company)

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Representative Name | Text | Y | Alphabetic only | - |
| Company | Text | Y | Alphanumeric | - |
| Company Email ID | Email | Y | Valid email format | - |
| Operator Office Number | Text | Y | Format: +971 122345678 | - |
| Trade License Number | Text | Y | Numeric, 8 digits | - |
| Trade License Expiry Date | Date | Y | DD/MM/YYYY, Future date | - |
| Lease Start Date | Date | Y | DD/MM/YYYY | - |
| Lease End Date | Date | Y | DD/MM/YYYY, After start date | - |
| Nationality | Dropdown | Y | Must select from list | - |
| Emirates ID Number | Text | Y | Numeric, 8 digits | - |
| Emirates ID Expiry Date | Date | Y | DD/MM/YYYY, Future date | - |
| DTCM Start Date | Date | Y | DD/MM/YYYY | - |
| DTCM Expiry Date | Date | Y | DD/MM/YYYY, After start date | - |
| DTCM | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |
| Emirates ID Front | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |
| Emirates ID Back | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |
| Company Trade License | File Upload | Y | PDF, JPG, JPEG, PNG, GIF, Max 2MB | - |

### Input Fields Table - Welcome Pack Configuration

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must select from list | - |
| Community | Dropdown | Y | Must select from list | - |
| Tower | Dropdown | N | Must select from list | - |
| Status | Dropdown | Y | Active/Inactive | Active |
| Welcome Pack | File Upload | Y | File type TBD | - |

### Input Fields Table - Email Recipients Configuration

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must select from list | - |
| Community | Dropdown | Y | Must select from list | - |
| Tower | Dropdown | N | Must select from list | - |
| MIP Email Recipient | Text | Y | Multiple emails, comma-separated, valid email format | - |
| MOP Email Recipient | Text | Y | Multiple emails, comma-separated, valid email format | - |
| Status | Dropdown | Y | Active/Inactive | Active |

### Buttons/Actions

**Move-in List Screen:**
- Create Request → Navigate to Move-in Type Selection
- View → Navigate to Move-in Details (Read-only or Editable based on status)
- Refresh → Reload list data
- Export All → Export list to file
- Search → Filter list based on search criteria
- Property Filter → Filter by property hierarchy

**Move-in Details Screen (New/RFI Status):**
- Cancel → Show confirmation modal → Update status to Cancelled
- Edit → Enable edit mode
- Mark RFI → Show RFI modal → Update status to RFI Submitted
- Approve → Update status to Approved
- History → Navigate to History tab

**Move-in Details Screen (Approved Status):**
- Close Request → Show Actual Move-in Date field → Update status to Closed
- History → Navigate to History tab

**Move-in Details Screen (Closed Status):**
- Move Out → Navigate to Move-out form (enabled 30 days before tenancy end)
- Account Renewal → Navigate to Account Renewal form (enabled 30 days before tenancy end)
- History → Navigate to History tab

**Move-in Create Flow:**
- Next → Navigate to next step
- Submit → Create move-in request
- Cancel → Navigate back to list

**Move-out List Screen:**
- Create Request → Navigate to Move-out form
- View → Navigate to Move-out Details
- Refresh → Reload list data
- Export All → Export list to file
- Search → Filter list based on search criteria
- Property Filter → Filter by property hierarchy

**Move-out Details Screen (New Status):**
- Cancel → Show confirmation modal → Update status to Cancelled
- Edit → Enable edit mode
- Approve → Update status to Approved
- History → Navigate to History tab

**Move-out Details Screen (Approved Status):**
- Close Request → Show Actual Move-out Date field → Update status to Moved-Out
- History → Navigate to History tab

**Account Renewal List Screen:**
- Create Request → Navigate to Account Renewal form
- View → Navigate to Account Renewal Details
- Refresh → Reload list data
- Export All → Export list to file
- Search → Filter list based on search criteria
- Property Filter → Filter by property hierarchy

**Account Renewal Details Screen (New/RFI Status):**
- Cancel → Show confirmation modal → Update status to Cancelled
- Edit → Enable edit mode
- Mark RFI → Show RFI modal → Update status to RFI Submitted
- Approve → Update status to Renewed
- History → Navigate to History tab

**Master Data Screens:**
- Add New → Navigate to Create form
- Edit → Navigate to Edit form
- History → View transaction history
- Save → Save configuration
- Cancel → Navigate back to list
- Refresh → Reload list data
- Search → Filter list based on search criteria

### Navigation Flow

**Move-in Flow (Tenant):**
```
Dashboard → Move-in List → Create Request → Select "Tenant" 
→ Step 1: Property Details (Next) 
→ Step 2: Verify Your Details (Next) 
→ Step 3: Move-in Details (Next) 
→ Step 4: Attach Documents (Submit) 
→ Move-in List (New Request Created)
```

**Move-in Flow (Owner):**
```
Dashboard → Move-in List → Create Request → Select "Owner" 
→ Step 1: Property Details (Next) 
→ Step 2: Verify Your Details (Next) 
→ Step 3: Move-in Details (Submit) 
→ Move-in List (New Request Created)
```

**Move-in Flow (HHO Unit):**
```
Dashboard → Move-in List → Create Request → Select "HHO Unit" 
→ Step 1: Move-in Details (Next) 
→ Step 2: Attach Document (Submit) 
→ Move-in List (New Request Created)
```

**Move-in Flow (HHO Company):**
```
Dashboard → Move-in List → Create Request → Select "HHO Company" 
→ Step 1: Property Details (Next) 
→ Step 2: Verify Your Details (Next) 
→ Step 3: Move-in Details (Next) 
→ Step 4: Attach Documents (Submit) 
→ Move-in List (New Request Created)
```

**Move-in Approval Flow:**
```
Move-in List → View (New Request) → Approve 
→ Move-in Details (Status: Approved) → Close Request 
→ Enter Actual Move-in Date → Submit 
→ Move-in Details (Status: Closed)
```

**Move-out Flow:**
```
Move-in List → View (Closed Request) → Move Out 
→ Move-out Form → Submit 
→ Move-out List (New Request Created) 
→ View → Approve 
→ Close Request → Enter Actual Move-out Date → Submit 
→ Move-out Details (Status: Moved-Out)
```

**Account Renewal Flow (Tenant):**
```
Move-in List → View (Closed Request) → Account Renewal 
→ Account Renewal Form (Step 1: Unit Details) → Next 
→ Step 2: Attach Documents (Ejari) → Submit 
→ Account Renewal List (New Request Created) 
→ View → Approve 
→ Account Renewal Details (Status: Renewed)
```

**Account Renewal Flow (HHO Unit):**
```
Move-in List → View (Closed Request) → Account Renewal 
→ Account Renewal Form (Step 1: Unit Details) → Next 
→ Step 2: Attach Documents (DTCM) → Submit 
→ Account Renewal List (New Request Created) 
→ View → Approve 
→ Account Renewal Details (Status: Renewed)
```

**Account Renewal Flow (HHO Company):**
```
Move-in List → View (Closed Request) → Account Renewal 
→ Account Renewal Form (Step 1: Move-in Details) → Next 
→ Step 2: Attach Documents (DTCM, Emirates ID, Trade License) → Submit 
→ Account Renewal List (New Request Created) 
→ View → Approve 
→ Account Renewal Details (Status: Renewed)
```

**Active Residents Flow:**
```
Dashboard → Active Residents → View Residency 
→ Resident Details (Shows Move-in + Account Renewal history) 
→ View (on specific request) → Request Details

Dashboard → Active Residents → View Assets 
→ Asset Details (Access Card, Parking)
```

**Master Data Flow:**
```
Dashboard → Occupancy Request → Master Data Setup 
→ Select (MIP Template/MOP Template/Welcome Pack/Email Recipients) 
→ List View → Add New/Edit 
→ Form → Save 
→ List View (Updated)
```

---

## 3. VALIDATION RULES

### Field: Email ID
- **Type:** Email
- **Required:** Y
- **Validations:** 
  - Standard email regex: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
  - Max length: TBD
- **Valid Examples:** 
  - essa.mohammed@gmail.com
  - community_admin1@sobharealty.com
  - test.user+tag@example.co.uk
- **Invalid Examples:** 
  - essa.mohammed (missing domain)
  - @gmail.com (missing local part)
  - essa@.com (invalid domain)
  - essa mohammed@gmail.com (space in email)
- **Error Messages:** 
  - "Please enter a valid email address"
  - "Email ID is required"
- **Dependencies:** None

### Field: First Name
- **Type:** Text
- **Required:** Y
- **Validations:** 
  - Alphabetic characters only (A-Z, a-z)
  - May include spaces for compound names
  - Min length: 1
  - Max length: TBD
- **Valid Examples:** 
  - Essa
  - John
  - Mary Jane
- **Invalid Examples:** 
  - Essa123 (contains numbers)
  - @Essa (contains special characters)
  - "" (empty)
- **Error Messages:** 
  - "First Name is required"
  - "First Name must contain only alphabetic characters"
- **Dependencies:** None

### Field: Middle Name
- **Type:** Text
- **Required:** N
- **Validations:** 
  - Alphabetic characters only (A-Z, a-z)
  - May include spaces
  - Max length: TBD
- **Valid Examples:** 
  - Mohammed
  - "" (empty - optional)
  - Van Der
- **Invalid Examples:** 
  - Mohammed123 (contains numbers)
  - @Mohammed (contains special characters)
- **Error Messages:** 
  - "Middle Name must contain only alphabetic characters"
- **Dependencies:** None

### Field: Last Name
- **Type:** Text
- **Required:** Y
- **Validations:** 
  - Alphabetic characters only (A-Z, a-z)
  - May include spaces for compound names
  - Min length: 1
  - Max length: TBD
- **Valid Examples:** 
  - Mohammed
  - Smith
  - Van Der Berg
- **Invalid Examples:** 
  - Mohammed123 (contains numbers)
  - @Mohammed (contains special characters)
  - "" (empty)
- **Error Messages:** 
  - "Last Name is required"
  - "Last Name must contain only alphabetic characters"
- **Dependencies:** None

### Field: Mobile Number
- **Type:** Text
- **Required:** Y
- **Validations:** 
  - Format: 0555 0898XX (10 digits with space after 4th digit)
  - Numeric only
  - Must start with 0
- **Valid Examples:** 
  - 0555 089812
  - 0501 234567
- **Invalid Examples:** 
  - 555089812 (missing leading 0)
  - 0555089812 (missing space)
  - 05550898 (too short)
  - 0555 08981234 (too long)
  - 0555 08981A (contains letter)
- **Error Messages:** 
  - "Mobile Number is required"
  - "Please enter a valid mobile number in format: 0555 0898XX"
- **Dependencies:** None

### Field: Emirates ID Number
- **Type:** Text
- **Required:** Y (for Tenant, HHO Company)
- **Validations:** 
  - Format: 784-xxxx-xxxxxxx-x (15 characters with dashes)
  - Numeric only (excluding dashes)
  - Must start with 784
- **Valid Examples:** 
  - 784-1234-1234567-1
  - 784-9999-9999999-9
- **Invalid Examples:** 
  - 784123412345671 (missing dashes)
  - 123-1234-1234567-1 (wrong prefix)
  - 784-12-1234567-1 (wrong format)
  - 784-1234-123456-1 (too short)
  - 784-1234-12345678-1 (too long)
- **Error Messages:** 
  - "Emirates ID Number is required"
  - "Please enter a valid Emirates ID in format: 784-xxxx-xxxxxxx-x"
- **Dependencies:** Emirates ID Expiry Date must be future date

### Field: Emirates ID Expiry Date
- **Type:** Date
- **Required:** Y (for Tenant, HHO Company)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Must be future date (after today)
  - Valid date (e.g., not 32/13/2025)
- **Valid Examples:** 
  - 12/05/2025 (if today is before this date)
  - 31/12/2026
- **Invalid Examples:** 
  - 12/05/2020 (past date)
  - 32/05/2025 (invalid day)
  - 12/13/2025 (invalid month)
  - 12-05-2025 (wrong format)
  - 2025/05/12 (wrong format)
- **Error Messages:** 
  - "Emirates ID Expiry Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
  - "Emirates ID Expiry Date must be a future date"
- **Dependencies:** Emirates ID Number

### Field: Move-in Date
- **Type:** Date
- **Required:** Y
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Can be past, present, or future
- **Valid Examples:** 
  - 12/05/2025
  - 08/05/2025
  - 20/05/2025
- **Invalid Examples:** 
  - 32/05/2025 (invalid day)
  - 12/13/2025 (invalid month)
  - 12-05-2025 (wrong format)
  - 2025/05/12 (wrong format)
- **Error Messages:** 
  - "Move-in Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** None

### Field: Tenancy Contract Number
- **Type:** Text
- **Required:** Y (for Tenant)
- **Validations:** 
  - Alphanumeric
  - Format: AB-12345678 (example pattern)
  - Max length: TBD
- **Valid Examples:** 
  - AB-12345678
  - TC-98765432
  - 12345678
- **Invalid Examples:** 
  - "" (empty)
  - AB@12345678 (special characters)
- **Error Messages:** 
  - "Tenancy Contract Number is required"
  - "Please enter a valid Tenancy Contract Number"
- **Dependencies:** Tenancy Contract Start Date, Tenancy Contract End Date

### Field: Tenancy Contract Start Date
- **Type:** Date
- **Required:** Y (for Tenant)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Can be past, present, or future
- **Valid Examples:** 
  - 12/05/2025
  - 08/05/2024
- **Invalid Examples:** 
  - 32/05/2025 (invalid day)
  - 12/13/2025 (invalid month)
  - 12-05-2025 (wrong format)
- **Error Messages:** 
  - "Tenancy Contract Start Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** Must be before Tenancy Contract End Date

### Field: Tenancy Contract End Date
- **Type:** Date
- **Required:** Y (for Tenant)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Must be after Tenancy Contract Start Date
- **Valid Examples:** 
  - 14/05/2026 (if start date is 12/05/2025)
  - 20/05/2026
- **Invalid Examples:** 
  - 11/05/2025 (before start date)
  - 12/05/2025 (same as start date)
  - 32/05/2026 (invalid day)
- **Error Messages:** 
  - "Tenancy Contract End Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
  - "Tenancy Contract End Date must be after Start Date"
- **Dependencies:** Tenancy Contract Start Date

### Field: Adult(s) (Above 12 years)
- **Type:** Number
- **Required:** Y
- **Validations:** 
  - Integer only
  - Min: 1
  - Max: TBD (assume 99)
- **Valid Examples:** 
  - 1
  - 3
  - 10
- **Invalid Examples:** 
  - 0 (below minimum)
  - -1 (negative)
  - 1.5 (decimal)
  - ABC (non-numeric)
- **Error Messages:** 
  - "Number of Adults is required"
  - "Number of Adults must be at least 1"
  - "Please enter a valid number"
- **Dependencies:** None

### Field: Children (Ages 0-12)
- **Type:** Number
- **Required:** Y
- **Validations:** 
  - Integer only
  - Min: 0
  - Max: TBD (assume 99)
- **Valid Examples:** 
  - 0
  - 1
  - 5
- **Invalid Examples:** 
  - -1 (negative)
  - 1.5 (decimal)
  - ABC (non-numeric)
- **Error Messages:** 
  - "Number of Children is required"
  - "Number of Children cannot be negative"
  - "Please enter a valid number"
- **Dependencies:** None

### Field: Household staff(s)
- **Type:** Radio Button
- **Required:** Y
- **Validations:** 
  - Must select Yes or No
  - If Yes, number field appears (integer, min: 1)
- **Valid Examples:** 
  - No
  - Yes + 1
  - Yes + 5
- **Invalid Examples:** 
  - Not selected
  - Yes + 0 (if Yes selected, must be at least 1)
  - Yes + -1
- **Error Messages:** 
  - "Please select whether household staff will be present"
  - "Please enter number of household staff"
- **Dependencies:** If Yes, number field becomes required

### Field: Pets(s)
- **Type:** Radio Button
- **Required:** Y
- **Validations:** 
  - Must select Yes or No
  - If Yes, number field appears (integer, min: 1)
- **Valid Examples:** 
  - No
  - Yes + 1
  - Yes + 2
- **Invalid Examples:** 
  - Not selected
  - Yes + 0 (if Yes selected, must be at least 1)
  - Yes + -1
- **Error Messages:** 
  - "Please select whether pets will be present"
  - "Please enter number of pets"
- **Dependencies:** If Yes, number field becomes required

### Field: People of determination
- **Type:** Radio Button
- **Required:** Y
- **Validations:** 
  - Must select Yes or No
  - If Yes, textarea field appears for details
- **Valid Examples:** 
  - No
  - Yes + "Need wheelchair assistance for elderly patient during move-in"
  - Yes + "" (details optional)
- **Invalid Examples:** 
  - Not selected
- **Error Messages:** 
  - "Please select whether people of determination will be present"
- **Dependencies:** If Yes, details textarea becomes visible (optional)

### Field: Unit Permit Number
- **Type:** Text
- **Required:** Y (for HHO Unit, HHO Company)
- **Validations:** 
  - Format: AB-12345678 (example pattern)
  - Alphanumeric with dash
  - Max length: TBD
- **Valid Examples:** 
  - AB-12345678
  - UP-98765432
  - 123
- **Invalid Examples:** 
  - "" (empty)
  - AB@12345678 (special characters other than dash)
- **Error Messages:** 
  - "Unit Permit Number is required"
  - "Please enter a valid Unit Permit Number"
- **Dependencies:** Unit Permit Start Date, Unit Permit End Date

### Field: Unit Permit Start Date
- **Type:** Date
- **Required:** Y (for HHO Unit, HHO Company)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
- **Valid Examples:** 
  - 12/05/2025
  - 08/05/2024
- **Invalid Examples:** 
  - 32/05/2025 (invalid day)
  - 12/13/2025 (invalid month)
  - 12-05-2025 (wrong format)
- **Error Messages:** 
  - "Unit Permit Start Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** Must be before Unit Permit End Date

### Field: Unit Permit End Date
- **Type:** Date
- **Required:** Y (for HHO Unit, HHO Company)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Must be after Unit Permit Start Date
- **Valid Examples:** 
  - 14/05/2026 (if start date is 12/05/2025)
  - 20/05/2026
- **Invalid Examples:** 
  - 11/05/2025 (before start date)
  - 12/05/2025 (same as start date)
  - 32/05/2026 (invalid day)
- **Error Messages:** 
  - "Unit Permit End Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
  - "Unit Permit End Date must be after Start Date"
- **Dependencies:** Unit Permit Start Date

### Field: Representative Name
- **Type:** Text
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Alphabetic characters only
  - May include spaces
  - Min length: 1
  - Max length: TBD
- **Valid Examples:** 
  - Essa
  - John Smith
- **Invalid Examples:** 
  - Essa123 (contains numbers)
  - @Essa (contains special characters)
  - "" (empty)
- **Error Messages:** 
  - "Representative Name is required"
  - "Representative Name must contain only alphabetic characters"
- **Dependencies:** None

### Field: Company
- **Type:** Text
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Alphanumeric
  - May include spaces and special characters (., &, -)
  - Min length: 1
  - Max length: TBD
- **Valid Examples:** 
  - ABC Company
  - Smith & Sons Ltd.
  - Tech-Solutions 2024
- **Invalid Examples:** 
  - "" (empty)
- **Error Messages:** 
  - "Company name is required"
- **Dependencies:** None

### Field: Company Email ID
- **Type:** Email
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Standard email regex
  - Max length: TBD
- **Valid Examples:** 
  - abccompany@gmail.com
  - info@company.co.uk
- **Invalid Examples:** 
  - abccompany (missing domain)
  - @gmail.com (missing local part)
  - abc company@gmail.com (space in email)
- **Error Messages:** 
  - "Company Email ID is required"
  - "Please enter a valid email address"
- **Dependencies:** None

### Field: Operator Office Number
- **Type:** Text
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Format: +971 122345678 (country code + space + 9 digits)
  - Numeric with + and space
- **Valid Examples:** 
  - +971 122345678
  - +971 501234567
- **Invalid Examples:** 
  - 122345678 (missing country code)
  - +971122345678 (missing space)
  - +971 12234567 (wrong digit count)
  - +971 12234567A (contains letter)
- **Error Messages:** 
  - "Operator Office Number is required"
  - "Please enter a valid phone number in format: +971 XXXXXXXXX"
- **Dependencies:** None

### Field: Trade License Number
- **Type:** Text
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Numeric only
  - 8 digits (based on example: 12345678)
  - May also accept alphanumeric format: AB-123456
- **Valid Examples:** 
  - 12345678
  - AB-123456
- **Invalid Examples:** 
  - 1234567 (too short)
  - 123456789 (too long)
  - 1234567A (contains letter in numeric format)
  - "" (empty)
- **Error Messages:** 
  - "Trade License Number is required"
  - "Please enter a valid Trade License Number"
- **Dependencies:** Trade License Expiry Date

### Field: Trade License Expiry Date
- **Type:** Date
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Must be future date
  - Valid date
- **Valid Examples:** 
  - 10/07/2025 (if today is before this date)
  - 31/12/2026
- **Invalid Examples:** 
  - 10/07/2020 (past date)
  - 32/07/2025 (invalid day)
  - 10/13/2025 (invalid month)
  - 10-07-2025 (wrong format)
- **Error Messages:** 
  - "Trade License Expiry Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
  - "Trade License Expiry Date must be a future date"
- **Dependencies:** Trade License Number

### Field: Lease Start Date
- **Type:** Date
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
- **Valid Examples:** 
  - 09/05/2025
  - 01/01/2024
- **Invalid Examples:** 
  - 32/05/2025 (invalid day)
  - 09/13/2025 (invalid month)
  - 09-05-2025 (wrong format)
- **Error Messages:** 
  - "Lease Start Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** Must be before Lease End Date

### Field: Lease End Date
- **Type:** Date
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Must be after Lease Start Date
- **Valid Examples:** 
  - 09/05/2026 (if start date is 09/05/2025)
  - 31/12/2026
- **Invalid Examples:** 
  - 08/05/2025 (before start date)
  - 09/05/2025 (same as start date)
  - 32/05/2026 (invalid day)
- **Error Messages:** 
  - "Lease End Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
  - "Lease End Date must be after Start Date"
- **Dependencies:** Lease Start Date

### Field: Nationality
- **Type:** Dropdown
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Must select from predefined list
- **Valid Examples:** 
  - United Arab Emirates
  - India
  - United Kingdom
- **Invalid Examples:** 
  - Not selected
  - Custom text entry
- **Error Messages:** 
  - "Nationality is required"
  - "Please select a valid nationality"
- **Dependencies:** None

### Field: Move-out Date
- **Type:** Date
- **Required:** Y
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Can be future date
- **Valid Examples:** 
  - 20/05/2025
  - 15/06/2025
- **Invalid Examples:** 
  - 32/05/2025 (invalid day)
  - 20/13/2025 (invalid month)
  - 20-05-2025 (wrong format)
- **Error Messages:** 
  - "Move-out Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** None

### Field: Reason for Move-Out
- **Type:** Dropdown
- **Required:** Y
- **Validations:** 
  - Must select from predefined list
- **Valid Examples:** 
  - Job Relocation
  - (Other predefined reasons)
- **Invalid Examples:** 
  - Not selected
  - Custom text entry
- **Error Messages:** 
  - "Reason for Move-Out is required"
  - "Please select a valid reason"
- **Dependencies:** None

### Field: Actual Move-out Date
- **Type:** Date
- **Required:** Y (when closing move-out request)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Can be past or present date
- **Valid Examples:** 
  - 12/06/2025
  - 15/06/2025
- **Invalid Examples:** 
  - 32/06/2025 (invalid day)
  - 12/13/2025 (invalid month)
  - 12-06-2025 (wrong format)
- **Error Messages:** 
  - "Actual Move-out Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** Move-out Date

### Field: Actual Move-in Date
- **Type:** Date
- **Required:** Y (when closing move-in request)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Can be past or present date
- **Valid Examples:** 
  - 12/06/2025
  - 15/06/2025
- **Invalid Examples:** 
  - 32/06/2025 (invalid day)
  - 12/13/2025 (invalid month)
  - 12-06-2025 (wrong format)
- **Error Messages:** 
  - "Actual Move-in Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** Move-in Date

### Field: Tenancy Start Date (Account Renewal)
- **Type:** Date
- **Required:** Y (for Tenant renewal)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
- **Valid Examples:** 
  - 15/05/2025
  - 01/01/2026
- **Invalid Examples:** 
  - 32/05/2025 (invalid day)
  - 15/13/2025 (invalid month)
  - 15-05-2025 (wrong format)
- **Error Messages:** 
  - "Tenancy Start Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** Must be before Tenancy End Date

### Field: Tenancy End Date (Account Renewal)
- **Type:** Date
- **Required:** Y (for Tenant renewal)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Must be after Tenancy Start Date
- **Valid Examples:** 
  - 14/05/2026 (if start date is 15/05/2025)
  - 31/12/2026
- **Invalid Examples:** 
  - 14/05/2025 (before start date)
  - 15/05/2025 (same as start date)
  - 32/05/2026 (invalid day)
- **Error Messages:** 
  - "Tenancy End Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
  - "Tenancy End Date must be after Start Date"
- **Dependencies:** Tenancy Start Date

### Field: DTCM Start Date
- **Type:** Date
- **Required:** Y (for HHO Company renewal)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
- **Valid Examples:** 
  - 15/05/2025
  - 01/01/2026
- **Invalid Examples:** 
  - 32/05/2025 (invalid day)
  - 15/13/2025 (invalid month)
  - 15-05-2025 (wrong format)
- **Error Messages:** 
  - "DTCM Start Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
- **Dependencies:** Must be before DTCM Expiry Date

### Field: DTCM Expiry Date
- **Type:** Date
- **Required:** Y (for HHO Company renewal)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Valid date
  - Must be after DTCM Start Date
- **Valid Examples:** 
  - 14/05/2026 (if start date is 15/05/2025)
  - 31/12/2026
- **Invalid Examples:** 
  - 14/05/2025 (before start date)
  - 15/05/2025 (same as start date)
  - 32/05/2026 (invalid day)
- **Error Messages:** 
  - "DTCM Expiry Date is required"
  - "Please enter a valid date in format DD/MM/YYYY"
  - "DTCM Expiry Date must be after Start Date"
- **Dependencies:** DTCM Start Date

### Field: File Uploads (All Documents)
- **Type:** File Upload
- **Required:** Y (varies by document type and move-in type)
- **Validations:** 
  - Supported file types: PDF, JPG, JPEG, PNG, GIF
  - Max file size: 2MB
  - One file per upload field
- **Valid Examples:** 
  - document.pdf (1.5MB)
  - emirates_id.jpg (500KB)
  - ejari.png (1MB)
- **Invalid Examples:** 
  - document.docx (unsupported file type)
  - large_file.pdf (3MB - exceeds max size)
  - "" (no file selected when required)
- **Error Messages:** 
  - "[Document Name] is required"
  - "File size must not exceed 2MB"
  - "Supported file types: PDF, JPG, JPEG, PNG, GIF"
- **Dependencies:** Varies by move-in type

### Field: MIP Email Recipient
- **Type:** Text (Multiple emails)
- **Required:** Y
- **Validations:** 
  - Multiple valid email addresses
  - Comma-separated
  - Each email must follow standard email regex
  - No spaces around commas (or trim spaces)
- **Valid Examples:** 
  - community_admin1@sobharealty.com
  - community_admin1@sobharealty.com,community_super_admin1@sobharealty.com
  - admin1@test.com,admin2@test.com,admin3@test.com
- **Invalid Examples:** 
  - "" (empty)
  - community_admin1 (invalid email)
  - admin1@test.com, admin2@test.com (space after comma - depends on implementation)
  - admin1@test.com;admin2@test.com (wrong separator)
- **Error Messages:** 
  - "MIP Email Recipient is required"
  - "Please enter valid email addresses separated by commas"
  - "Invalid email format: [specific email]"
- **Dependencies:** None

### Field: MOP Email Recipient
- **Type:** Text (Multiple emails)
- **Required:** Y
- **Validations:** 
  - Multiple valid email addresses
  - Comma-separated
  - Each email must follow standard email regex
  - No spaces around commas (or trim spaces)
- **Valid Examples:** 
  - community_admin1@sobharealty.com
  - community_admin1@sobharealty.com,community_super_admin1@sobharealty.com
  - admin1@test.com,admin2@test.com,admin3@test.com
- **Invalid Examples:** 
  - "" (empty)
  - community_admin1 (invalid email)
  - admin1@test.com, admin2@test.com (space after comma - depends on implementation)
  - admin1@test.com;admin2@test.com (wrong separator)
- **Error Messages:** 
  - "MOP Email Recipient is required"
  - "Please enter valid email addresses separated by commas"
  - "Invalid email format: [specific email]"
- **Dependencies:** None

### Field: Master Community (Dropdown)
- **Type:** Dropdown
- **Required:** Y
- **Validations:** 
  - Must select from predefined list
  - List populated from master data
- **Valid Examples:** 
  - Sobha Hartland
  - Sobha Hartland -II
  - Sobha Orbis
  - Sobha Elwood
- **Invalid Examples:** 
  - Not selected
  - Custom text entry
- **Error Messages:** 
  - "Master Community is required"
  - "Please select a valid Master Community"
- **Dependencies:** Cascades to Community dropdown

### Field: Community (Dropdown)
- **Type:** Dropdown
- **Required:** Y
- **Validations:** 
  - Must select from predefined list
  - List filtered based on Master Community selection
- **Valid Examples:** 
  - The crest
  - Sobha Orbis
  - 360 RCS
  - Sobha Elwood
- **Invalid Examples:** 
  - Not selected
  - Custom text entry
- **Error Messages:** 
  - "Community is required"
  - "Please select a valid Community"
- **Dependencies:** Master Community selection; Cascades to Tower/Building dropdown

### Field: Tower/Building/Street (Dropdown)
- **Type:** Dropdown
- **Required:** Y
- **Validations:** 
  - Must select from predefined list
  - List filtered based on Community selection
- **Valid Examples:** 
  - Tower 1
  - Orbis Tower B
  - 360 RCS
  - Sobha Elwood Villas
- **Invalid Examples:** 
  - Not selected
  - Custom text entry
- **Error Messages:** 
  - "Tower/Building is required"
  - "Please select a valid Tower/Building"
- **Dependencies:** Community selection; Cascades to Unit dropdown

### Field: Unit Number (Dropdown)
- **Type:** Dropdown or Text (varies by screen)
- **Required:** Y
- **Validations:** 
  - If dropdown: Must select from predefined list
  - If text: Alphanumeric, format: A-123 or 102
- **Valid Examples:** 
  - A-123
  - 102
  - B-456
- **Invalid Examples:** 
  - Not selected (if dropdown)
  - "" (empty)
  - A@123 (special characters)
- **Error Messages:** 
  - "Unit Number is required"
  - "Please select/enter a valid Unit Number"
- **Dependencies:** Tower/Building selection

### Field: Status (Master Data)
- **Type:** Dropdown
- **Required:** Y
- **Validations:** 
  - Must select Active or Inactive
- **Valid Examples:** 
  - Active
  - Inactive
- **Invalid Examples:** 
  - Not selected
- **Error Messages:** 
  - "Status is required"
- **Dependencies:** None

---

## 4. EDGE CASES & BOUNDARIES

### Date Fields
**Boundary Values:**
- **Min Date:** 01/01/1900 (system minimum)
- **Max Date:** 31/12/2099 (system maximum)
- **Leap Year:** 29/02/2024 (valid), 29/02/2023 (invalid)
- **Month End:** 31/01/2025 (valid), 31/02/2025 (invalid), 30/02/2025 (invalid)

**Edge Cases:**
- Empty/Null: Should show "Date is required" error
- Invalid format: 2025-05-12 → Should show "Please enter date in DD/MM/YYYY format"
- Past date when future required: 01/01/2020 → "Date must be in the future"
- Future date when past required: 01/01/2099 → "Date cannot be in the future"
- Same date for start/end: Should show "End date must be after Start date"
- End date before start date: Should show "End date must be after Start date"

### Numeric Fields (Adults, Children, Pets, Household Staff)
**Boundary Values:**
- **Adults:** Min=1, Max=99 (assumed)
  - Test: 0 (invalid), 1 (valid), 99 (valid), 100 (invalid)
- **Children:** Min=0, Max=99 (assumed)
  - Test: -1 (invalid), 0 (valid), 99 (valid), 100 (invalid)
- **Pets/Staff (if Yes):** Min=1, Max=99 (assumed)
  - Test: 0 (invalid), 1 (valid), 99 (valid), 100 (invalid)

**Edge Cases:**
- Decimal values: 1.5 → Should show "Please enter a whole number"
- Negative values: -1 → Should show "Value cannot be negative"
- Non-numeric: ABC → Should show "Please enter a valid number"
- Leading zeros: 01 → Should accept as 1
- Very large numbers: 999999 → Should show "Value exceeds maximum"

### Text Fields (Names, Company, etc.)
**Boundary Values:**
- **Min Length:** 1 character (for required fields)
- **Max Length:** TBD (assume 100 characters for names, 200 for company)
- Test: "" (invalid if required), "A" (valid), 100-char string (valid), 101-char string (invalid)

**Edge Cases:**
- Leading/trailing spaces: " John " → Should trim to "John"
- Multiple spaces: "John  Smith" → Should accept or normalize to "John Smith"
- Special characters in name fields: "John@123" → Should show "Only alphabetic characters allowed"
- All uppercase: "JOHN" → Should accept
- All lowercase: "john" → Should accept
- Mixed case: "JoHn" → Should accept
- Single character: "A" → Should accept
- Unicode characters: "José" → Should accept (if internationalization supported)
- Emoji: "John😊" → Should reject

### Email Fields
**Boundary Values:**
- **Min Length:** 6 characters (a@b.co)
- **Max Length:** TBD (assume 254 characters per RFC)

**Edge Cases:**
- Missing @ symbol: "johngmail.com" → Invalid
- Multiple @ symbols: "john@@gmail.com" → Invalid
- Missing domain: "john@" → Invalid
- Missing local part: "@gmail.com" → Invalid
- Spaces: "john smith@gmail.com" → Invalid
- Special characters in local part: "john.smith+tag@gmail.com" → Valid
- Subdomain: "john@mail.company.co.uk" → Valid
- IP address domain: "john@192.168.1.1" → Valid (if supported)
- Leading/trailing dots: ".john@gmail.com" or "john.@gmail.com" → Invalid
- Consecutive dots: "john..smith@gmail.com" → Invalid

### Phone Number Fields
**Mobile Number (0555 0898XX):**
- **Exact Length:** 11 characters (including space)
- Test: 10 chars (invalid), 11 chars (valid), 12 chars (invalid)

**Edge Cases:**
- Missing leading 0: "555 089812" → Invalid
- Missing space: "0555089812" → Invalid
- Extra spaces: "0555  089812" → Invalid
- Letters: "0555 08981A" → Invalid
- Special characters: "0555-089812" → Invalid

**Operator Office Number (+971 122345678):**
- **Exact Length:** 14 characters (including + and space)
- Test: 13 chars (invalid), 14 chars (valid), 15 chars (invalid)

**Edge Cases:**
- Missing +: "971 122345678" → Invalid
- Missing space: "+971122345678" → Invalid
- Wrong country code: "+1 122345678" → Invalid (if UAE-specific)
- Letters: "+971 12234567A" → Invalid

### Emirates ID Number (784-xxxx-xxxxxxx-x)
**Boundary Values:**
- **Exact Length:** 18 characters (including dashes)
- Test: 17 chars (invalid), 18 chars (valid), 19 chars (invalid)

**Edge Cases:**
- Missing dashes: "784123412345671" → Invalid
- Wrong prefix: "123-1234-1234567-1" → Invalid
- Extra dashes: "784--1234-1234567-1" → Invalid
- Letters: "784-123A-1234567-1" → Invalid
- Spaces instead of dashes: "784 1234 1234567 1" → Invalid

### File Upload Fields
**Boundary Values:**
- **File Size:** 0KB (invalid), 1KB (valid), 2MB (valid), 2.1MB (invalid)
- Test: Empty file (0KB), 1.99MB file, exactly 2MB file, 2.01MB file

**Edge Cases:**
- No file selected: Should show "[Document] is required"
- Wrong file type: .docx, .txt, .exe → Should show "Unsupported file type"
- Correct file type: .pdf, .jpg, .jpeg, .png, .gif → Should accept
- File name with special characters: "document@#$.pdf" → Should accept or sanitize
- Very long file name: 255+ characters → Should accept or truncate
- File name with spaces: "my document.pdf" → Should accept
- Duplicate file upload: Upload same file twice → Should accept (no uniqueness constraint mentioned)
- Corrupted file: Upload corrupted PDF → Should accept (validation likely happens on backend)
- Case sensitivity: .PDF, .JPG (uppercase extensions) → Should accept

### Dropdown Fields
**Edge Cases:**
- No selection: Should show "[Field] is required"
- Default value: If "Select..." is default, should not be submittable
- Disabled options: Should not be selectable
- Dynamic loading: If list is empty (no data), should show appropriate message

### Radio Button Fields (Yes/No)
**Edge Cases:**
- No selection: Should show "Please select an option"
- Default selection: If "No" is default, should be pre-selected
- Conditional fields: If "Yes" selected, dependent field should appear and become required

### Textarea Fields
**Boundary Values:**
- **Min Length:** 0 characters (if optional)
- **Max Length:** TBD (assume 500 characters)
- Test: Empty (valid if optional), 1 char (valid), 500 chars (valid), 501 chars (invalid)

**Edge Cases:**
- Only spaces: "     " → Should trim and treat as empty
- Line breaks: "Line1\nLine2" → Should accept
- Special characters: "Text with @#$%" → Should accept
- HTML/Script tags: "<script>alert('test')</script>" → Should sanitize or reject
- Very long single word: 500-character string without spaces → Should accept

### Comma-Separated Email Fields
**Boundary Values:**
- **Min Emails:** 1
- **Max Emails:** TBD (assume 10)
- Test: 0 emails (invalid), 1 email (valid), 10 emails (valid), 11 emails (invalid)

**Edge Cases:**
- Single email: "admin@test.com" → Valid
- Multiple emails: "admin1@test.com,admin2@test.com" → Valid
- Trailing comma: "admin1@test.com," → Should handle gracefully (trim or reject)
- Leading comma: ",admin1@test.com" → Should handle gracefully (trim or reject)
- Spaces after comma: "admin1@test.com, admin2@test.com" → Should trim spaces
- No spaces after comma: "admin1@test.com,admin2@test.com" → Valid
- Duplicate emails: "admin@test.com,admin@test.com" → Should accept or show warning
- One invalid email in list: "admin1@test.com,invalid,admin3@test.com" → Should show error for "invalid"
- Empty string between commas: "admin1@test.com,,admin3@test.com" → Should handle gracefully

### Property Hierarchy (Master Community → Community → Tower → Unit)
**Edge Cases:**
- Select Master Community without Community: Should show "Community is required"
- Change Master Community after selecting Community: Community dropdown should reset
- No units available for selected Tower: Should show "No units available"
- Unit already occupied: Should show "Unit is already occupied" (if applicable)

### Request Status Transitions
**Valid Transitions:**
- New → RFI Submitted
- New → Approved
- New → Cancelled
- RFI Submitted → Approved
- RFI Submitted → Cancelled
- Approved → Closed
- Approved → Cancelled (if allowed)

**Invalid Transitions:**
- Closed → New (should not be possible)
- Cancelled → Approved (should not be possible)
- Closed → Approved (should not be possible)

### Move-out/Account Renewal Enablement
**Edge Cases:**
- Exactly 30 days before tenancy end: Should be enabled
- 31 days before tenancy end: Should be disabled
-