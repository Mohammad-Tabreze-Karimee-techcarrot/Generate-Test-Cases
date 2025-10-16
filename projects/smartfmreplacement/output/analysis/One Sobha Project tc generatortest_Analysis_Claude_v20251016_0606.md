# Requirements Analysis by Claude AI

**Project:** smartfmreplacement
**Module:** One Sobha Project tc generatortest
**Analyzed:** 2025-10-16 06:06:29

---

# STRUCTURED TEST SPECIFICATION EXTRACTION

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
- **FR-127.4**: Separate MIP and MOP email recipient lists
- **FR-127.5**: Transaction history logging

### UC-128: Move-in Process
**Move-in Types:**
1. **Owner** (3 steps): Property Details → Verify Details → Move-In Details
2. **Tenant** (4 steps): Property Details → Verify Details → Move-In Details → Attach Documents
3. **HHO Unit** (2 steps): Move-In Details → Attach Document
4. **HHO Company** (4 steps): Property Details → Verify Details → Move-In Details → Attach Documents

**Request Statuses:**
- New → RFI Submitted → Approved → Closed
- Cancellation allowed at any stage

### Move-out Process
- **FR-MO.1**: Initiated from closed Move-in request
- **FR-MO.2**: Available 30 days before tenancy end date
- **FR-MO.3**: Statuses: New → Approved → Moved-Out
- **FR-MO.4**: Actual move-out date capture required

### Account Renewal Process
**Renewal Types:**
1. **Tenant**: Tenancy dates + Ejari document
2. **HHO Unit**: Tenancy dates + Unit Permit
3. **HHO Company**: Lease dates + DTCM + Trade License + Emirates ID

**FR-AR.1**: Status flow: New → RFI Submitted → Renewed

---

## 2. UI COMPONENTS & FLOWS

### MASTER DATA - MIP/MOP Template List

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must exist in system | - |
| Community | Dropdown | Y | Must belong to selected Master Community | - |
| Tower | Dropdown | N | Must belong to selected Community | - |
| Status | Radio | Y | Active/Inactive | Active |

**Actions:**
- View MIP Template → Opens template viewer (read-only)
- View MOP Template → Opens template viewer (read-only)
- Search → Filters list by entered criteria
- Refresh → Reloads data
- History → Shows transaction log

---

### MASTER DATA - Welcome Pack

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must exist in system | - |
| Community | Dropdown | Y | Must belong to Master Community | - |
| Tower | Dropdown | N | Must belong to Community | - |
| Welcome Pack | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Status | Radio | Y | Active/Inactive | Active |

**Actions:**
- Add New → Opens create form
- Edit → Opens edit form with pre-filled data
- History → Shows transaction log
- Save → Validates and saves data
- Cancel → Discards changes

---

### MASTER DATA - Email Recipients

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must exist in system | - |
| Community | Dropdown | Y | Must belong to Master Community | - |
| Tower | Dropdown | N | Must belong to Community | - |
| MIP Email Recipients | Text Area | Y | Valid email format; comma-separated | - |
| MOP Email Recipients | Text Area | Y | Valid email format; comma-separated | - |
| Status | Radio | Y | Active/Inactive | Active |

---

### MOVE-IN - Owner Type

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must exist in system | - |
| Community | Dropdown | Y | Must belong to Master Community | - |
| Building/Street | Dropdown | Y | Must belong to Community | - |
| Unit Number | Dropdown | Y | Must belong to Building/Street | - |
| Move-in Date | Date Picker | Y | DD/MM/YYYY; Future date allowed | - |
| Email ID | Text | Y | Valid email format | - |
| First Name | Text | Y | Min 1 char; Max length TBD | - |
| Middle Name | Text | N | Max length TBD | - |
| Last Name | Text | Y | Min 1 char; Max length TBD | - |
| Mobile Number | Text | Y | Format: 0555 0898XX (10 digits) | - |
| Adult(s) (Above 12 years) | Number | Y | Min: 1; Max: TBD | 1 |
| Children (Ages 0-12) | Number | Y | Min: 0; Max: TBD | 0 |
| Household staff(s) | Radio + Number | Y | Yes/No; If Yes, number required | No |
| Pets(s) | Radio + Number | Y | Yes/No; If Yes, number required | No |
| People of determination | Radio + Text | Y | Yes/No; If Yes, details required | No |

---

### MOVE-IN - Tenant Type

**Additional Fields (beyond Owner fields):**

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Emirates ID Number | Text | Y | Format: 784-xxxx-xxxxxxx-x | - |
| Emirates ID Expiry Date | Date Picker | Y | DD/MM/YYYY; Must be future date | - |
| Tenancy Contract Number | Text | Y | Format: AB-12345678 | - |
| Tenancy Contract Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Tenancy Contract End Date | Date Picker | Y | DD/MM/YYYY; Must be after start date | - |
| Emirates ID Front | File Upload | Y | JPG, JPEG, PNG; Max 2MB | - |
| Emirates ID Back | File Upload | Y | JPG, JPEG, PNG; Max 2MB | - |
| Ejari | File Upload | Y | PDF, JPG, JPEG, PNG; Max 2MB | - |

---

### MOVE-IN - HHO Unit Type

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | Must exist in system | - |
| Community | Dropdown | Y | Must belong to Master Community | - |
| Building/Street | Dropdown | Y | Must belong to Community | - |
| Unit Number | Dropdown | Y | Must belong to Building/Street | - |
| Move-in Date | Date Picker | Y | DD/MM/YYYY | - |
| First Name | Text | Y | Min 1 char | - |
| Middle Name | Text | N | - | - |
| Last Name | Text | Y | Min 1 char | - |
| Mobile Number | Text | Y | Format: 0555 0898XX | - |
| Email ID | Text | Y | Valid email format | - |
| Unit Permit Number | Text | Y | Format: AB-12345678 | - |
| Unit Permit Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Unit Permit End Date | Date Picker | Y | DD/MM/YYYY; Must be after start date | - |
| Unit Permit | File Upload | Y | PDF, JPG, JPEG, PNG; Max 2MB | - |

---

### MOVE-IN - HHO Company Type

**Additional Fields (beyond HHO Unit):**

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Representative Name | Text | Y | Min 1 char | - |
| Company | Text | Y | Min 1 char | - |
| Company Email ID | Text | Y | Valid email format | - |
| Operator Office Number | Text | Y | Format: +971 122345678 | - |
| Trade License Number | Text | Y | Numeric; 8 digits | - |
| Trade License Expiry Date | Date Picker | Y | DD/MM/YYYY; Must be future date | - |
| Lease Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Lease End Date | Date Picker | Y | DD/MM/YYYY; Must be after start date | - |
| Nationality | Dropdown | Y | Must exist in system | - |
| Emirates ID Number | Text | Y | Numeric; 8 digits | - |
| Emirates ID Expiry Date | Date Picker | Y | DD/MM/YYYY; Must be future date | - |
| Emirates ID Front | File Upload | Y | JPG, JPEG, PNG; Max 2MB | - |
| Emirates ID Back | File Upload | Y | JPG, JPEG, PNG; Max 2MB | - |
| Company Trade License | File Upload | Y | PDF, JPG, JPEG, PNG; Max 2MB | - |

---

### MOVE-OUT

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Move-out Date | Date Picker | Y | DD/MM/YYYY; Future date allowed | - |
| Reason for Move-Out | Dropdown | Y | Job Relocation, etc. | - |
| Actual Move-out Date | Date Picker | Y | DD/MM/YYYY; Captured at closure | - |
| Request Closed Date | Date | Auto | System generated | - |

**Disclaimer Text:**
"All the outstanding charges for cooling and hot water in the unit are paid by the resident. For the security deposit resident will contact the billing & collection service provider."

---

### ACCOUNT RENEWAL - Tenant

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Tenancy Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Tenancy End Date | Date Picker | Y | DD/MM/YYYY; Must be after start date | - |
| Ejari | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |

---

### ACCOUNT RENEWAL - HHO Unit

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Tenancy Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Tenancy End Date | Date Picker | Y | DD/MM/YYYY; Must be after start date | - |
| Dubai Tourism Unit Permit | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |

---

### ACCOUNT RENEWAL - HHO Company

| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Lease Contract End Date | Date Picker | Y | DD/MM/YYYY | - |
| DTCM Start Date | Date Picker | Y | DD/MM/YYYY | - |
| DTCM Expiry Date | Date Picker | Y | DD/MM/YYYY; Must be after start date | - |
| Trade License Expiry Date | Date Picker | Y | DD/MM/YYYY; Must be future date | - |
| DTCM | File Upload | Y | PDF, JPG, JPEG, PNG; Max 2MB | - |
| Emirates ID Front | File Upload | Y | JPG, JPEG, PNG; Max 2MB | - |
| Emirates ID Back | File Upload | Y | JPG, JPEG, PNG; Max 2MB | - |
| Company Trade License | File Upload | Y | PDF, JPG, JPEG, PNG; Max 2MB | - |

---

### ACTIVE RESIDENTS - List View

| Column Name | Type | Sortable | Filterable |
|-------------|------|----------|------------|
| Request ID | Text | Y | Y |
| Move-in Type | Text | Y | Y |
| Master Community | Text | Y | Y |
| Community | Text | Y | Y |
| Tower | Text | Y | Y |
| Unit | Text | Y | Y |
| Tenancy End Date | Date | Y | Y |

**Actions:**
- View Residency → Shows residency details
- View Assets → Shows access card and parking details

---

## 3. VALIDATION RULES

### Email ID
- **Type:** Text
- **Required:** Y
- **Format:** Standard email regex
- **Valid Examples:** 
  - essa.mohammed@gmail.com
  - community_admin1@sobharealty.com
  - test.user+tag@domain.co.uk
- **Invalid Examples:**
  - essa.mohammed@
  - @gmail.com
  - essa mohammed@gmail.com
  - essa.mohammed@.com
- **Error Message:** "Please enter a valid email address"
- **Dependencies:** None

---

### Mobile Number
- **Type:** Text
- **Required:** Y
- **Format:** 0555 0898XX (10 digits with space after 4th digit)
- **Valid Examples:**
  - 0555 089812
  - 0501 234567
- **Invalid Examples:**
  - 555 089812 (missing leading 0)
  - 0555089812 (missing space)
  - 05550898 (too short)
  - 055508981234 (too long)
  - 0555 08981A (contains letter)
- **Error Message:** "Please enter a valid mobile number in format: 0XXX XXXXXX"
- **Dependencies:** None

---

### Emirates ID Number
- **Type:** Text
- **Required:** Y (for Tenant, HHO Company)
- **Format:** 784-xxxx-xxxxxxx-x OR 8 digits (numeric)
- **Valid Examples:**
  - 784-1234-5678901-2
  - 12345678
- **Invalid Examples:**
  - 784-123-5678901-2 (incorrect segment length)
  - 1234567 (too short)
  - 784-xxxx-xxxxxxx (contains letters)
- **Error Message:** "Please enter a valid Emirates ID number"
- **Dependencies:** Emirates ID Expiry Date must be future date

---

### Emirates ID Expiry Date
- **Type:** Date Picker
- **Required:** Y (for Tenant, HHO Company)
- **Format:** DD/MM/YYYY
- **Valid Examples:**
  - 31/12/2025 (future date)
  - 01/01/2026
- **Invalid Examples:**
  - 31/12/2023 (past date)
  - 32/12/2025 (invalid day)
  - 31/13/2025 (invalid month)
  - 2025/12/31 (wrong format)
- **Error Message:** "Emirates ID expiry date must be a future date"
- **Dependencies:** Must be after current date

---

### Tenancy Contract Number
- **Type:** Text
- **Required:** Y (for Tenant)
- **Format:** AB-12345678 (2 letters, hyphen, 8 digits)
- **Valid Examples:**
  - AB-12345678
  - XY-98765432
- **Invalid Examples:**
  - AB12345678 (missing hyphen)
  - A-12345678 (only 1 letter)
  - AB-1234567 (only 7 digits)
  - 12-12345678 (starts with numbers)
- **Error Message:** "Please enter a valid tenancy contract number (Format: AB-12345678)"
- **Dependencies:** None

---

### Tenancy Contract Start/End Date
- **Type:** Date Picker
- **Required:** Y (for Tenant)
- **Format:** DD/MM/YYYY
- **Valid Examples:**
  - Start: 01/01/2025, End: 31/12/2025
  - Start: 15/06/2025, End: 14/06/2026
- **Invalid Examples:**
  - Start: 31/12/2025, End: 01/01/2025 (end before start)
  - Start: 31/12/2025, End: 31/12/2025 (same date)
- **Error Message:** "Tenancy end date must be after start date"
- **Dependencies:** End date must be > Start date

---

### Move-in Date
- **Type:** Date Picker
- **Required:** Y
- **Format:** DD/MM/YYYY
- **Valid Examples:**
  - 20/05/2025 (future date allowed)
  - 15/01/2024 (past date allowed)
- **Invalid Examples:**
  - 32/05/2025 (invalid day)
  - 15/13/2025 (invalid month)
- **Error Message:** "Please enter a valid move-in date"
- **Dependencies:** None (both past and future dates allowed)

---

### Adult(s) (Above 12 years)
- **Type:** Number
- **Required:** Y
- **Min:** 1
- **Max:** TBD (assume 99)
- **Valid Examples:**
  - 1
  - 5
  - 10
- **Invalid Examples:**
  - 0 (below minimum)
  - -1 (negative)
  - 1.5 (decimal)
  - ABC (non-numeric)
- **Error Message:** "At least 1 adult is required"
- **Dependencies:** None

---

### Children (Ages 0-12)
- **Type:** Number
- **Required:** Y
- **Min:** 0
- **Max:** TBD (assume 99)
- **Valid Examples:**
  - 0
  - 3
  - 10
- **Invalid Examples:**
  - -1 (negative)
  - 2.5 (decimal)
  - ABC (non-numeric)
- **Error Message:** "Please enter a valid number of children"
- **Dependencies:** None

---

### Household Staff(s)
- **Type:** Radio + Number
- **Required:** Y
- **Options:** Yes/No
- **If Yes:** Number field required (Min: 1, Max: TBD)
- **Valid Examples:**
  - No (no number required)
  - Yes + 2
- **Invalid Examples:**
  - Yes + 0 (number required if Yes)
  - Yes + blank (number required if Yes)
- **Error Message:** "Please specify number of household staff"
- **Dependencies:** Number field enabled only if "Yes" selected

---

### Pets(s)
- **Type:** Radio + Number
- **Required:** Y
- **Options:** Yes/No
- **If Yes:** Number field required (Min: 1, Max: TBD)
- **Valid Examples:**
  - No
  - Yes + 1
- **Invalid Examples:**
  - Yes + 0
  - Yes + blank
- **Error Message:** "Please specify number of pets"
- **Dependencies:** Number field enabled only if "Yes" selected

---

### People of Determination
- **Type:** Radio + Text Area
- **Required:** Y
- **Options:** Yes/No
- **If Yes:** Details text area required
- **Valid Examples:**
  - No
  - Yes + "Need wheelchair assistance for elderly patient during move-in"
- **Invalid Examples:**
  - Yes + blank (details required if Yes)
- **Error Message:** "Please provide details for people of determination"
- **Dependencies:** Text area enabled only if "Yes" selected

---

### Unit Permit Number
- **Type:** Text
- **Required:** Y (for HHO Unit, HHO Company)
- **Format:** AB-12345678 OR 123 (alphanumeric)
- **Valid Examples:**
  - AB-12345678
  - 123
- **Invalid Examples:**
  - (blank)
- **Error Message:** "Please enter unit permit number"
- **Dependencies:** Unit Permit Start/End dates required

---

### Trade License Number
- **Type:** Text
- **Required:** Y (for HHO Company)
- **Format:** 8 digits (numeric)
- **Valid Examples:**
  - 12345678
  - 98765432
- **Invalid Examples:**
  - 1234567 (7 digits)
  - 123456789 (9 digits)
  - AB123456 (contains letters)
- **Error Message:** "Please enter a valid 8-digit trade license number"
- **Dependencies:** Trade License Expiry Date must be future date

---

### File Upload Fields
- **Type:** File Upload
- **Required:** Y (varies by field)
- **Supported Formats:** PDF, JPG, JPEG, PNG, GIF
- **Max Size:** 2MB
- **Valid Examples:**
  - document.pdf (1.5MB)
  - image.jpg (500KB)
- **Invalid Examples:**
  - document.docx (unsupported format)
  - image.jpg (3MB - exceeds limit)
  - (no file selected when required)
- **Error Messages:**
  - "Please upload a file"
  - "File size must not exceed 2MB"
  - "Supported file types: PDF, JPG, JPEG, PNG, GIF"
- **Dependencies:** None

---

### Move-out Date
- **Type:** Date Picker
- **Required:** Y
- **Format:** DD/MM/YYYY
- **Valid Examples:**
  - 20/05/2025 (future date)
- **Invalid Examples:**
  - (blank)
  - 32/05/2025 (invalid day)
- **Error Message:** "Please enter a valid move-out date"
- **Dependencies:** Available only 30 days before tenancy end date

---

### Reason for Move-Out
- **Type:** Dropdown
- **Required:** Y
- **Options:** Job Relocation, [other options TBD]
- **Valid Examples:**
  - Job Relocation
- **Invalid Examples:**
  - (blank/not selected)
- **Error Message:** "Please select a reason for move-out"
- **Dependencies:** None

---

### Email Recipients (Multiple)
- **Type:** Text Area
- **Required:** Y
- **Format:** Comma-separated valid email addresses
- **Valid Examples:**
  - community_admin1@sobharealty.com
  - community_admin1@sobharealty.com,community_super_admin1@sobharealty.com
- **Invalid Examples:**
  - community_admin1@ (invalid email)
  - community_admin1@sobharealty.com; community_admin2@sobharealty.com (semicolon separator)
  - community_admin1@sobharealty.com , community_admin2@sobharealty.com (space after comma)
- **Error Message:** "Please enter valid email addresses separated by commas"
- **Dependencies:** None

---

## 4. EDGE CASES & BOUNDARIES

### Date Fields
- **Boundary Values:**
  - Min: 01/01/1900
  - Max: 31/12/2099
  - Invalid: 00/01/2025, 32/01/2025, 01/13/2025
- **Leap Year:** 29/02/2024 (valid), 29/02/2023 (invalid)
- **Null/Empty:** Must show error if required field

### Numeric Fields (Adults, Children, Staff, Pets)
- **Boundary Values:**
  - Adults: Min=1, Test: 0 (invalid), 1 (valid), 99 (valid), 100 (invalid if max=99)
  - Children: Min=0, Test: -1 (invalid), 0 (valid), 99 (valid), 100 (invalid if max=99)
- **Decimal:** 1.5 (invalid - must be integer)
- **Null/Empty:** Must show error if required

### Text Fields (Names, Email, Mobile)
- **Whitespace:**
  - Leading/trailing spaces: "  John  " → Should trim to "John"
  - Multiple spaces: "John   Doe" → Should handle gracefully
- **Special Characters:**
  - Names: Test with hyphens (Al-Maktoum), apostrophes (O'Brien), accents (José)
  - Email: Test with +, -, _, . characters
- **Case Sensitivity:** Email should be case-insensitive
- **Max Length:** Test at boundary (e.g., 255 chars, 256 chars)

### File Uploads
- **Size Boundaries:**
  - 1.99MB (valid)
  - 2.00MB (valid)
  - 2.01MB (invalid)
- **Format Validation:**
  - .pdf, .PDF (case insensitive)
  - .exe, .bat (invalid)
- **Empty File:** 0KB file upload
- **Corrupted File:** Upload corrupted PDF

### Dropdown/Selection Fields
- **No Selection:** Default state validation
- **Invalid Option:** Manually inject invalid option ID
- **Dependent Dropdowns:** 
  - Select Community without Master Community
  - Select Tower without Community

### Conditional Fields
- **Household Staff:**
  - Select "Yes" → Number field appears → Leave blank → Error
  - Select "No" → Number field hidden → No validation
- **People of Determination:**
  - Select "Yes" → Text area appears → Leave blank → Error
  - Select "No" → Text area hidden → No validation

### Status Transitions
- **Invalid Transitions:**
  - New → Closed (skip Approved)
  - Approved → New (backward transition)
  - Closed → Approved (reopen)
- **Valid Transitions:**
  - New → RFI Submitted → New → Approved → Closed
  - New → Cancelled

### Property Hierarchy
- **Orphaned Records:**
  - Tower exists without Community
  - Unit exists without Tower
- **Duplicate Active Records:**
  - Two active MIP templates for same property combination
  - Two active Welcome Packs for same property

### Email Recipients
- **Boundary:**
  - 1 email (valid)
  - 10 emails (valid)
  - 100 emails (test performance)
- **Malformed:**
  - Missing @ symbol
  - Multiple @ symbols
  - Trailing comma: "email1@test.com,"

### Move-out Availability
- **Date Logic:**
  - Tenancy End: 31/12/2025
  - Available from: 01/12/2025 (30 days before)
  - Test on: 30/11/2025 (should be disabled)
  - Test on: 01/12/2025 (should be enabled)

---

## 5. DATA CONSTRAINTS & FORMATS

### Date Formats
- **Display Format:** DD/MM/YYYY
- **Examples:** 20/05/2025, 01/01/2024
- **Invalid:** 2025-05-20, 05/20/2025, 20-05-2025

### Email Format
- **Pattern:** `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- **Examples:** user@domain.com, user.name+tag@sub.domain.co.uk
- **Invalid:** user@, @domain.com, user domain@test.com

### Mobile Number Format
- **Pattern:** `0XXX XXXXXX` (10 digits with space after 4th)
- **Examples:** 0555 089812, 0501 234567
- **Invalid:** 555089812, 0555089812, +971555089812

### Emirates ID Format
- **Pattern 1:** `784-XXXX-XXXXXXX-X` (15 chars with hyphens)
- **Pattern 2:** `XXXXXXXX` (8 digits)
- **Examples:** 784-1234-5678901-2, 12345678
- **Invalid:** 784-123-5678901-2, 1234567

### Tenancy Contract Number Format
- **Pattern:** `XX-XXXXXXXX` (2 letters, hyphen, 8 digits)
- **Examples:** AB-12345678, XY-98765432
- **Invalid:** AB12345678, A-12345678, AB-1234567

### Trade License Number Format
- **Pattern:** `XXXXXXXX` (8 digits)
- **Examples:** 12345678, 98765432
- **Invalid:** 1234567, 123456789, AB123456

### Phone Number Format (Operator Office)
- **Pattern:** `+971 XXXXXXXXX` (country code + space + 9 digits)
- **Examples:** +971 122345678
- **Invalid:** 971122345678, +971122345678, +971 12345678

### File Upload Constraints
- **Formats:** PDF, JPG, JPEG, PNG, GIF
- **Max Size:** 2MB (2,097,152 bytes)
- **Naming:** No special characters except hyphen, underscore, period

### Text Field Lengths
| Field | Min Length | Max Length |
|-------|------------|------------|
| First Name | 1 | 50 (assumed) |
| Middle Name | 0 | 50 (assumed) |
| Last Name | 1 | 50 (assumed) |
| Email | 5 | 100 (assumed) |
| Mobile Number | 10 | 11 (with space) |
| Emirates ID | 8 or 18 | 18 (with hyphens) |
| Tenancy Contract | 11 | 11 (fixed) |
| Trade License | 8 | 8 (fixed) |
| Unit Permit | 3 | 20 (assumed) |

### Numeric Field Ranges
| Field | Min | Max | Decimals |
|-------|-----|-----|----------|
| Adults | 1 | 99 (assumed) | No |
| Children | 0 | 99 (assumed) | No |
| Household Staff | 1 | 99 (assumed) | No |
| Pets | 1 | 99 (assumed) | No |

### Status Values
- **Move-in:** New, RFI Submitted, Approved, Closed, Cancelled
- **Move-out:** New, Approved, Moved-Out, Cancelled
- **Account Renewal:** New, RFI Submitted, Renewed, Cancelled
- **Master Data:** Active, Inactive

---

## 6. INTEGRATION & SECURITY

### User Roles & Permissions

| Role | UC-125 View Templates | UC-126 Welcome Pack | UC-127 Email Recipients | Move-in | Move-out | Account Renewal |
|------|----------------------|---------------------|------------------------|---------|----------|-----------------|
| Super Admin | View | CRUD | CRUD | CRUD + Approve | CRUD + Approve | CRUD + Approve |
| Community Admin | View | CRUD | - | CRUD + Approve | CRUD + Approve | CRUD + Approve |
| User | - | - | - | Create | Create | Create |

### Authentication
- **Method:** Session-based (implied from login screen)
- **Login Fields:** Username, Password
- **Session Timeout:** TBD
- **Remember Me:** Optional checkbox

### Authorization Checks
- **Per Screen:** Validate user role before rendering
- **Per Action:** Validate permissions before executing (Edit, Approve, Cancel, etc.)
- **Data Scope:** Users see only data for their assigned communities

### Sensitive Data Fields
| Field | Encryption | Masking | Access Control |
|-------|------------|---------|----------------|
| Emirates ID Number | Y | Partial (784-xxxx-xxxxxxx-x) | Admin only |
| Mobile Number | N | Partial (0555 0898XX) | Admin only |
| Email | N | No | Admin only |
| Documents (PDFs) | Y | No | Admin + Owner |

### API Endpoints (Assumed)

#### Master Data
- `GET /api/mip-templates` - List MIP templates
- `GET /api/mop-templates` - List MOP templates
- `POST /api/welcome-pack` - Create Welcome Pack
- `PUT /api/welcome-pack/{id}` - Update Welcome Pack
- `GET /api/welcome-pack/history/{id}` - Get history
- `POST /api/email-recipients` - Create Email Recipients
- `PUT /api/email-recipients/{id}` - Update Email Recipients

#### Move-in
- `POST /api/move-in` - Create Move-in request
- `GET /api/move-in/{id}` - Get Move-in details
- `PUT /api/move-in/{id}` - Update Move-in request
- `PUT /api/move-in/{id}/status` - Change status (Approve, RFI, Cancel)
- `POST /api/move-in/{id}/close` - Close request
- `GET /api/move-in/history/{id}` - Get history

#### Move-out
- `POST /api/move-out` - Create Move-out request
- `GET /api/move-out/{id}` - Get Move-out details
- `PUT /api/move-out/{id}/status` - Change status (Approve, Cancel)
- `POST /api/move-out/{id}/close` - Close request with actual date

#### Account Renewal
- `POST /api/account-renewal` - Create Renewal request
- `GET /api/account-renewal/{id}` - Get Renewal details
- `PUT /api/account-renewal/{id}` - Update Renewal request
- `PUT /api/account-renewal/{id}/status` - Change status (Approve, RFI, Cancel)

#### Active Residents
- `GET /api/active-residents` - List active residents
- `GET /api/active-residents/{id}/residency` - Get residency details
- `GET /api/active-residents/{id}/assets` - Get assets (access cards, parking)

#### Common
- `GET /api/properties/master-communities` - List master communities
- `GET /api/properties/communities?masterCommunityId={id}` - List communities
- `GET /api/properties/towers?communityId={id}` - List towers
- `GET /api/properties/units?towerId={id}` - List units
- `POST /api/file-upload` - Upload document
- `GET /api/file-download/{id}` - Download document

### Request/Response Formats

**Create Move-in Request (Tenant):**
```json
{
  "moveInType": "Tenant",
  "masterCommunityId": 123,
  "communityId": 456,
  "towerId": 789,
  "unitId": 101,
  "moveInDate": "2025-05-20",
  "user": {
    "email": "essa.mohammed@gmail.com",
    "firstName": "Essa",
    "middleName": "Mohammed",
    "lastName": "Mohammed",
    "mobileNumber": "0555089812"
  },
  "moveInDetails": {
    "emiratesIdNumber": "784-1234-5678901-2",
    "emiratesIdExpiry": "2025-12-31",
    "tenancyContractNumber": "AB-12345678",
    "tenancyStartDate": "2025-05-20",
    "tenancyEndDate": "2026-05-19",
    "adults": 3,
    "children": 2,
    "householdStaff": 0,
    "pets": 2,
    "peopleOfDetermination": true,
    "determinationDetails": "Need wheelchair assistance"
  },
  "documents": {
    "emiratesIdFront": "file-id-123",
    "emiratesIdBack": "file-id-124",
    "ejari": "file-id-125"
  }
}
```

**Response (Success):**
```json
{
  "success": true,
  "requestId": "123459",
  "status": "New",
  "message": "Move-in request created successfully"
}
```

**Response (Validation Error):**
```json
{
  "success": false,
  "errors": [
    {
      "field": "emiratesIdExpiry",
      "message": "Emirates ID expiry date must be a future date"
    }
  ]
}
```

### Security Headers
- `Authorization: Bearer {token}` (assumed)
- `Content-Type: application/json`
- `X-CSRF-Token: {token}` (for state-changing operations)

### Audit Logging
- **All Actions Logged:** Create, Update, Approve, Cancel, Close, RFI
- **Log Fields:** Action Type, Action By (User ID/Name), Action Date, Remarks/Comments
- **Retention:** TBD

---

## 7. BUSINESS LOGIC & CALCULATIONS

### Property Hierarchy Validation
```
IF Master Community selected
  THEN load Communities WHERE masterCommunityId = selected
IF Community selected
  THEN load Towers WHERE communityId = selected
IF Tower selected
  THEN load Units WHERE towerId = selected
```

### Active Template/Configuration Rule
```
FOR each property combination (Master Community + Community + Tower)
  COUNT active records WHERE type = 'MIP Template'
  IF count > 1 THEN error: "Only one active MIP template allowed per property"
```

### Move-out Availability Logic
```
IF tenancyEndDate IS NOT NULL
  AND currentDate >= (tenancyEndDate - 30 days)
  THEN enable "Move Out" button
ELSE disable "Move Out" button
```

### Status Transition Rules

**Move-in:**
```
New → RFI Submitted (Admin action: Mark RFI)
RFI Submitted → New (User action: Resubmit after correction)
New → Approved (Admin action: Approve)
Approved → Closed (Admin action: Close Request + Actual Move-in Date)
Any Status → Cancelled (Admin action: Cancel)
```

**Move-out:**
```
New → Approved (Admin action: Approve)
Approved → Moved-Out (Admin action: Close Request + Actual Move-out Date)
Any Status → Cancelled (Admin action: Cancel)
```

**Account Renewal:**
```
New → RFI Submitted (Admin action: Mark RFI)
RFI Submitted → New (User action: Resubmit)
New → Renewed (Admin action: Approve)
Any Status → Cancelled (Admin action: Cancel)
```

### Conditional Field Display
```
IF householdStaff = "Yes"
  THEN show householdStaffCount field (required, min=1)
ELSE hide householdStaffCount field

IF pets = "Yes"
  THEN show petsCount field (required, min=1)
ELSE hide petsCount field

IF peopleOfDetermination = "Yes"
  THEN show determinationDetails textarea (required)
ELSE hide determinationDetails textarea
```

### Document Requirements by Move-in Type
```
Owner:
  - No documents required

Tenant:
  - Emirates ID Front (required)
  - Emirates ID Back (required)
  - Ejari (required)

HHO Unit:
  - Unit Permit (required)

HHO Company:
  - Unit Permit (required)
  - Emirates ID Front (required)
  - Emirates ID Back (required)
  - Company Trade License (required)
```

### Account Renewal Document Requirements
```
Tenant:
  - Ejari (required)

HHO Unit:
  - Dubai Tourism Unit Permit (required)

HHO Company:
  - DTCM (required)
  - Emirates ID Front (required)
  - Emirates ID Back (required)
  - Company Trade License (required)
```

### SLA Breach Calculation
```
IF (currentDate - requestCreatedDate) > SLA_THRESHOLD
  THEN mark as "SLA Breached"
  AND increment breachedSLACount in dashboard
```

### Dashboard Counters
```
Move-in:
  - New: COUNT WHERE status = 'New'
  - RFI Submitted: COUNT WHERE status = 'RFI Submitted'
  - Breached SLA: COUNT WHERE (currentDate - createdDate) > SLA_THRESHOLD
  - Total: SUM of all statuses

Move-out:
  - New: COUNT WHERE status = 'New'
  - Ready to Move-Out: COUNT WHERE status = 'Approved'
  - Gate pass generated: COUNT WHERE status = 'Moved-Out'
  - Breached SLA: COUNT WHERE (currentDate - createdDate) > SLA_THRESHOLD

Account Renewal:
  - New Requests: COUNT WHERE status = 'New'
  - RFI Submitted: COUNT WHERE status = 'RFI Submitted'
  - Breached SLA: COUNT WHERE (currentDate - createdDate) > SLA_THRESHOLD
```

### Active Residents Filter Logic
```
Active Residents = All Move-in requests WHERE status = 'Closed'
  AND (tenancyEndDate IS NULL OR tenancyEndDate >= currentDate)

Filter by:
  - Owner: COUNT WHERE moveInType = 'Owner'
  - Tenant: COUNT WHERE moveInType = 'Tenant'
  - HHO: COUNT WHERE moveInType IN ('HHO Unit', 'HHO Company')
```

### Email Notification Triggers
```
ON Move-in Approved:
  SEND email TO configured MIP recipients FOR property
  
ON Move-out Approved:
  IF "Should customer be notified" = Yes
    THEN SEND email TO configured MOP recipients FOR property
    
ON Account Renewal Approved:
  SEND email TO user AND configured recipients
```

### History Log Entry
```
ON any state change:
  INSERT INTO history (
    requestId,
    actionType,
    actionBy,
    actionDate,
    remarks
  )
```

---

## 8. CRITICAL TEST SCENARIOS

### High Priority Test Cases

1. **Unique Active Configuration Rule**
   - Create MIP template for property X (Active)
   - Attempt to create another MIP template for same property X (Active)
   - Expected: Error message

2. **Status Transition Validation**
   - Create Move-in request (Status: New)
   - Attempt to directly change to Closed (skip Approved)
   - Expected: Error or disabled action

3. **Move-out Availability (30-day rule)**
   - Tenancy End Date: 31/12/2025
   - Test on 30/11/2025: Move-out button disabled
   - Test on 01/12/2025: Move-out button enabled

4. **Conditional Field Validation**
   - Select "Household Staff: Yes" → Leave count blank → Submit
   - Expected: Validation error

5. **File Upload Size Limit**
   - Upload 2.01MB file
   - Expected: Error message

6. **Email Format Validation**
   - Enter "user@" in email field → Submit
   - Expected: Validation error

7. **Date Range Validation**
   - Tenancy Start: 31/12/2025, End: 01/01/2025
   - Expected: Error "End date must be after start date"

8. **Role-Based Access Control**
   - Login as Community Admin
   - Attempt to access Email Recipients configuration
   - Expected: Access denied

9. **Dependent Dropdown Logic**
   - Select Community without Master Community
   - Expected: Community dropdown disabled or empty

10. **Multiple Email Recipients**
    - Enter: "email1@test.com,email2@test.com,invalid@"
    - Expected: Error on third email

---

**END OF STRUCTURED EXTRACTION**