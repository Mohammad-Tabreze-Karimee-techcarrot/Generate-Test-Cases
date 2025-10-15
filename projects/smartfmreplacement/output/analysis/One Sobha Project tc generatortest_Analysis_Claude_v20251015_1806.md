# Requirements Analysis by Claude AI

**Project:** smartfmreplacement
**Module:** One Sobha Project tc generatortest
**Analyzed:** 2025-10-15 18:06:11

---

# STRUCTURED TEST SPECIFICATION EXTRACTION

## 1. FUNCTIONAL REQUIREMENTS

### UC-125: View MIP/MOP Template
**ID:** UC-125  
**Description:** View Move-In Process (MIP) and Move-Out Process (MOP) templates  
**Business Rules:**
- Super Admin and Community Admin only
- Templates managed from backend (view-only in backoffice)
- One active template per unique property combination (Master Community/Community/Tower)
- All transactions logged in history

### UC-126: Master Data Setup - Welcome Pack
**ID:** UC-126  
**Description:** Configure Welcome Pack per property  
**Business Rules:**
- Super Admin and Community Admin only
- One active Welcome Pack per unique property combination
- All transactions logged in history

### UC-127: Master Data Setup - Email Recipients
**ID:** UC-127  
**Description:** Configure community-specific email recipients  
**Business Rules:**
- Super Admin only
- Multiple email recipients per community (comma-separated)
- One active configuration per unique property combination
- Email validation required

### UC-128: Move-In Request Management
**ID:** UC-128  
**Description:** Create and manage move-in requests for 4 types: Owner, Tenant, HHO Unit, HHO Company  
**Business Rules:**
- SLA tracking (New, RFI Submitted, Breached)
- Status workflow: New → RFI Submitted → Approved → Closed
- Cancel allowed at any stage
- Edit allowed in New/RFI status
- Actual move-in date captured on closure

### Move-Out Request Management
**Description:** Manage move-out requests  
**Business Rules:**
- Move-out option enabled 30 days before tenancy end date
- Status workflow: New → Approved → Moved-Out
- Actual move-out date captured
- Outstanding charges acknowledgment required

### Account Renewal Request Management
**Description:** Renew tenancy accounts (Tenant, HHO Unit, HHO Company only)  
**Business Rules:**
- Not applicable for Owner type
- Status workflow: New → RFI Submitted → Approved → Renewed
- Document renewal required based on type

---

## 2. UI COMPONENTS & FLOWS

### A. MASTER DATA SETUP

#### MIP/MOP Template List View
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | From master data | - |
| Community | Dropdown | Y | Filtered by Master Community | - |
| Tower | Dropdown | N | Filtered by Community | - |
| Status | Radio | Y | Active/Inactive | Active |

**Actions:**
- View MIP Template → Opens template (read-only)
- View MOP Template → Opens template (read-only)
- Search → Filters list
- Refresh → Reloads data

#### Welcome Pack Form
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | From master data | - |
| Community | Dropdown | Y | Filtered by Master Community | - |
| Tower | Dropdown | N | Filtered by Community | - |
| Welcome Pack | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Status | Radio | Y | Active/Inactive | Active |

**Actions:**
- Add New → Opens create form
- Edit → Opens edit form (existing records)
- History → Shows transaction log
- Save → Validates and saves
- Cancel → Discards changes

#### Email Recipients Form
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | From master data | - |
| Community | Dropdown | Y | Filtered by Master Community | - |
| Tower | Dropdown | N | Filtered by Community | - |
| MIP Email Recipient | Text Area | Y | Email regex; comma-separated | - |
| MOP Email Recipient | Text Area | Y | Email regex; comma-separated | - |
| Status | Radio | Y | Active/Inactive | Active |

---

### B. MOVE-IN REQUEST FLOWS

#### Move-In Type Selection Screen
**Options:**
1. **Owner** → 3 Steps: Property Details → Verify Details → Move-In Details
2. **Tenant** → 4 Steps: Property Details → Verify Details → Move-In Details → Attach Documents
3. **HHO Unit** → 2 Steps: Move-In Details → Attach Document
4. **HHO Company** → 4 Steps: Property Details → Verify Details → Move-In Details → Attach Documents

---

#### OWNER Move-In Form

**Step 1: Property Details**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | From master data | - |
| Community | Dropdown | Y | Filtered by Master Community | - |
| Building/Street | Dropdown | Y | Filtered by Community | - |
| Unit Number | Dropdown | Y | Filtered by Building | - |
| Move-in Date | Date Picker | Y | DD/MM/YYYY; Future date | - |

**Step 2: Owner Details**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| First Name | Text | Y | Max 50 chars; Letters only | - |
| Middle Name | Text | N | Max 50 chars; Letters only | - |
| Last Name | Text | Y | Max 50 chars; Letters only | - |
| Mobile Number | Text | Y | Format: 0555 0898XX | - |
| Email ID | Email | Y | Email regex | - |

**Step 3: Move-In Details**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Adult(s) (Above 12 years) | Number | Y | Min: 1; Max: 99 | 1 |
| Children (Ages 0-12) | Number | Y | Min: 0; Max: 99 | 0 |
| Household staff(s) | Radio + Number | Y | Yes/No; If Yes: Min 1 | No |
| Pets(s) | Radio + Number | Y | Yes/No; If Yes: Min 1 | No |
| People of determination | Radio + Text | Y | Yes/No; If Yes: Details required | No |
| Details | Text Area | Conditional | Max 500 chars | - |

---

#### TENANT Move-In Form

**Steps 1-3:** Same as Owner

**Step 4: Attach Documents**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Emirates ID Front | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Emirates ID Back | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Ejari | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |

**Additional Fields (Step 2):**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Emirates ID Number | Text | Y | Format: 784-xxxx-xxxxxxx-x | - |
| Emirates ID Expiry Date | Date Picker | Y | DD/MM/YYYY; Future date | - |
| Tenancy Contract Number | Text | Y | Format: AB-12345678 | - |
| Tenancy Contract Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Tenancy Contract End Date | Date Picker | Y | DD/MM/YYYY; After Start Date | - |

---

#### HHO UNIT Move-In Form

**Step 1: Move-In Details**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y | From master data | - |
| Community | Dropdown | Y | Filtered by Master Community | - |
| Building/Street | Dropdown | Y | Filtered by Community | - |
| Unit Number | Dropdown | Y | Filtered by Building | - |
| Move-in Date | Date Picker | Y | DD/MM/YYYY; Future date | - |
| First Name | Text | Y | Max 50 chars; Letters only | - |
| Middle Name | Text | N | Max 50 chars; Letters only | - |
| Last Name | Text | Y | Max 50 chars; Letters only | - |
| Mobile Number | Text | Y | Format: 0555 0898XX | - |
| Email ID | Email | Y | Email regex | - |
| Unit Permit Number | Text | Y | Format: AB-12345678 | - |
| Unit Permit Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Unit Permit End Date | Date Picker | Y | DD/MM/YYYY; After Start Date | - |

**Step 2: Attach Document**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Unit Permit | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |

---

#### HHO COMPANY Move-In Form

**Steps 1-3:** Property Details, User Details (same as Owner)

**Step 3: Move-In Details (Additional Fields)**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Representative Name | Text | Y | Max 50 chars | - |
| Company | Text | Y | Max 100 chars | - |
| Company Email ID | Email | Y | Email regex | - |
| Operator Office Number | Text | Y | Format: +971 122345678 | - |
| Trade License Number | Text | Y | Numeric; Max 8 digits | - |
| Trade License Expiry Date | Date Picker | Y | DD/MM/YYYY; Future date | - |
| Lease Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Lease End Date | Date Picker | Y | DD/MM/YYYY; After Start Date | - |
| Nationality | Dropdown | Y | From country master | - |
| Emirates ID Number | Text | Y | Numeric; Max 8 digits | - |
| Emirates ID Expiry Date | Date Picker | Y | DD/MM/YYYY; Future date | - |
| Unit Permit Number | Text | Y | Format: AB-12345678 | - |
| Unit Permit Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Unit Permit End Date | Date Picker | Y | DD/MM/YYYY; After Start Date | - |

**Step 4: Attach Documents**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Unit Permit | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Emirates ID Front | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Emirates ID Back | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Company Trade License | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |

---

#### Move-In List View
| Column | Type | Sortable | Filterable |
|--------|------|----------|------------|
| Request ID | Text | Y | Y |
| Move-in Type | Text | Y | Y |
| Master Community | Text | Y | Y |
| Community | Text | Y | Y |
| Tower | Text | Y | Y |
| Unit | Text | Y | Y |
| Created Date | Date | Y | Y |
| Move in Date | Date | Y | Y |
| Request Status | Badge | Y | Y |

**Status Values:** New, RFI Submitted, Approved, Closed, Cancel

**Actions:**
- View → Opens request details (read-only)
- Create Request → Opens type selection
- Property Filter → Filters by property hierarchy
- Search → Full-text search
- Refresh → Reloads data
- Export All → Downloads CSV/Excel

**Dashboard Counters:**
- Breached SLA: Count
- New: Count
- RFI Pending: Count
- Total: Count

---

#### Move-In Request Detail View (Admin)

**Status: New**
**Actions Available:**
- Cancel → Confirmation modal → Status = Cancel
- Edit → Opens edit form
- Mark RFI → Status = RFI Submitted
- Approve → Status = Approved

**Status: Approved**
**Actions Available:**
- Close Request → Requires Actual Move-in Date → Status = Closed

**Status: Closed**
**Actions Available:**
- Move Out (enabled 30 days before tenancy end)
- Account Renewal (for Tenant/HHO types only)

---

### C. MOVE-OUT REQUEST FLOW

#### Move-Out Form
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Move-out Date | Date Picker | Y | DD/MM/YYYY; Future date | - |
| Reason for Move-Out | Dropdown | Y | Job Relocation, Personal, Other | - |
| Acknowledgment | Checkbox | Y | Must be checked | Unchecked |

**Acknowledgment Text:**
"All the outstanding charges for cooling and hot water in the unit are paid by the resident. For the security deposit resident will contact the billing & collection service provider."

**Actions:**
- Submit → Creates move-out request
- Cancel → Discards changes

#### Move-Out Detail View (Admin)

**Status: New**
**Actions:**
- Cancel → Confirmation modal with notification option
- Edit → Opens edit form
- Approve → Status = Approved

**Status: Approved**
**Actions:**
- Close Request → Requires Actual Move-out Date → Status = Moved-Out

**Cancel Confirmation Modal:**
- "Should the customer be notified about the move-out?"
- Options: Yes / No
- Text Area: "Canceled the request" (reason)

---

### D. ACCOUNT RENEWAL REQUEST FLOW

#### Account Renewal Type Selection
**Applicable For:** Tenant, HHO Unit, HHO Company (NOT Owner)

---

#### TENANT Account Renewal Form

**Step 1: Unit & User Details**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Master Community | Dropdown | Y (Read-only) | Pre-filled | - |
| Community | Dropdown | Y (Read-only) | Pre-filled | - |
| Building/Street | Dropdown | Y (Read-only) | Pre-filled | - |
| Unit Number | Dropdown | Y (Read-only) | Pre-filled | - |
| Email ID | Email | Y (Read-only) | Pre-filled | - |
| First Name | Text | Y (Read-only) | Pre-filled | - |
| Middle Name | Text | N (Read-only) | Pre-filled | - |
| Last Name | Text | Y (Read-only) | Pre-filled | - |
| Mobile Number | Text | Y (Read-only) | Pre-filled | - |
| Tenancy Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Tenancy End Date | Date Picker | Y | DD/MM/YYYY; After Start Date | - |

**Occupants Details:** (Same as Move-In)

**Step 2: Attach Documents**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Ejari | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |

---

#### HHO UNIT Account Renewal Form

**Step 1: Details**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Unit Permit Start Date | Date Picker | Y | DD/MM/YYYY | - |
| Unit Permit End Date | Date Picker | Y | DD/MM/YYYY; After Start Date | - |

**Step 2: Attach Documents**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Dubai Tourism Unit Permit | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |

---

#### HHO COMPANY Account Renewal Form

**Step 1: Details**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Lease Contract End Date | Date Picker | Y | DD/MM/YYYY; Future date | - |
| DTCM Start Date | Date Picker | Y | DD/MM/YYYY | - |
| DTCM Expiry Date | Date Picker | Y | DD/MM/YYYY; After Start Date | - |
| Trade License Expiry Date | Date Picker | Y | DD/MM/YYYY; Future date | - |

**Step 2: Attach Documents**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| DTCM | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Emirates ID Front | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Emirates ID Back | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |
| Company Trade License | File Upload | Y | PDF, JPG, JPEG, PNG, GIF; Max 2MB | - |

---

#### Account Renewal Detail View (Admin)

**Status: New**
**Actions:**
- Cancel → Confirmation modal
- Edit → Opens edit form
- Mark RFI → Status = RFI Submitted
- Approve → Status = Renewed

**Status: Renewed**
- View only (no actions)

---

### E. ACTIVE RESIDENTS

#### Active Residents List View
| Column | Type | Sortable | Filterable |
|--------|------|----------|------------|
| Request ID | Text | Y | Y |
| Move-in Type | Text | Y | Y |
| Master Community | Text | Y | Y |
| Community | Text | Y | Y |
| Tower | Text | Y | Y |
| Unit | Text | Y | Y |
| Tenancy End Date | Date | Y | Y |

**Actions:**
- View Residency → Opens residency history
- View Assets → Opens access card & parking details

**Dashboard Counters:**
- Owner: Count
- Tenant: Count
- HHO: Count
- HHC: Count
- Total: Count

---

#### Residency Details View
**Shows:**
- Unit Details (read-only)
- User Details (read-only)
- Move-in Details (read-only)
- Residency History Table:

| Request Type | Request ID | Permit Number | Tenancy End Date | Action |
|--------------|------------|---------------|------------------|--------|
| Move-in | 12345 | MIP-12345 | 20 May 2025 | View |
| Account Renewal | 12345 | ARN-12345 | 20 May 2024 | View |

---

#### Asset Details View

**Access Card Tab:**
| Field | Value |
|-------|-------|
| Card Number | CN_170124-1 |
| Card Slot | 459-001 |

**Parking Tab:**
Multiple parking bays displayed:
| Field | Value |
|-------|-------|
| Parking Bay | B1-233 |
| Plate Source | Dubai |
| Plate Code | K |
| Plate Number | 1234 |
| Vehicle Color | Yellow |
| Vehicle Make | Nissan |

---

### F. HISTORY LOG

**All Requests Include History Tab:**
| Column | Type |
|--------|------|
| Action Type | Text |
| Created/Modified by | Text |
| Created/Modified Date | DateTime |
| Comments/Remarks | Text |

**Action Types:**
- Request Created
- Request Amended
- Marked as RFI
- Request Approved
- Request Closed
- Request Cancelled

---

## 3. VALIDATION RULES

### Email Field
- **Type:** Email
- **Required:** Y
- **Validations:** Standard email regex pattern
- **Valid Examples:** 
  - essa.mohammed@gmail.com
  - community_admin1@sobharealty.com
- **Invalid Examples:**
  - essa.mohammed@
  - @gmail.com
  - essa mohammed@gmail.com
- **Error Messages:** "Please enter a valid email address"
- **Dependencies:** None

### Mobile Number Field
- **Type:** Text
- **Required:** Y
- **Validations:** Format: 0555 0898XX (10 digits starting with 0)
- **Valid Examples:** 
  - 0555089812
  - 0555 089812
- **Invalid Examples:**
  - 555089812 (missing leading 0)
  - 05550898 (too short)
  - +971555089812 (wrong format)
- **Error Messages:** "Please enter a valid mobile number"
- **Dependencies:** None

### Emirates ID Number Field
- **Type:** Text
- **Required:** Y (for Tenant, HHO Company)
- **Validations:** Format: 784-xxxx-xxxxxxx-x (15 digits with dashes)
- **Valid Examples:** 
  - 784-1234-1234567-1
- **Invalid Examples:**
  - 784123412345671 (no dashes)
  - 784-123-123456-1 (wrong format)
- **Error Messages:** "Please enter a valid Emirates ID number"
- **Dependencies:** Emirates ID Expiry Date

### Date Fields (General)
- **Type:** Date Picker
- **Required:** Y
- **Validations:** Format: DD/MM/YYYY
- **Valid Examples:** 
  - 15/05/2025
  - 01/01/2024
- **Invalid Examples:**
  - 32/05/2025 (invalid day)
  - 15/13/2025 (invalid month)
  - 15-05-2025 (wrong format)
- **Error Messages:** "Please enter a valid date in DD/MM/YYYY format"
- **Dependencies:** Varies by field

### Move-in Date Field
- **Type:** Date Picker
- **Required:** Y
- **Validations:** 
  - Format: DD/MM/YYYY
  - Must be future date or today
- **Valid Examples:** 
  - Today's date
  - Any future date
- **Invalid Examples:**
  - Past dates
- **Error Messages:** "Move-in date cannot be in the past"
- **Dependencies:** None

### Tenancy Contract Start/End Date
- **Type:** Date Picker
- **Required:** Y
- **Validations:** 
  - Format: DD/MM/YYYY
  - End Date must be after Start Date
- **Valid Examples:** 
  - Start: 12/05/2025, End: 14/05/2026
- **Invalid Examples:**
  - Start: 12/05/2025, End: 11/05/2025 (end before start)
  - Start: 12/05/2025, End: 12/05/2025 (same date)
- **Error Messages:** "Tenancy end date must be after start date"
- **Dependencies:** Start Date ↔ End Date

### Emirates ID Expiry Date
- **Type:** Date Picker
- **Required:** Y (for Tenant, HHO Company)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Must be future date
- **Valid Examples:** 
  - Any future date
- **Invalid Examples:**
  - Today's date
  - Past dates
- **Error Messages:** "Emirates ID expiry date must be in the future"
- **Dependencies:** Emirates ID Number

### Unit Permit Start/End Date
- **Type:** Date Picker
- **Required:** Y (for HHO Unit, HHO Company)
- **Validations:** 
  - Format: DD/MM/YYYY
  - End Date must be after Start Date
- **Valid Examples:** 
  - Start: 12/05/2025, End: 12/05/2026
- **Invalid Examples:**
  - Start: 12/05/2025, End: 11/05/2025
- **Error Messages:** "Unit permit end date must be after start date"
- **Dependencies:** Start Date ↔ End Date

### Name Fields (First/Middle/Last)
- **Type:** Text
- **Required:** Y (First/Last); N (Middle)
- **Validations:** 
  - Max 50 characters
  - Letters only (alphabets and spaces)
- **Valid Examples:** 
  - Essa
  - Mohammed
  - Al Maktoum
- **Invalid Examples:**
  - Essa123 (contains numbers)
  - @Essa (special characters)
  - [51 characters string] (exceeds max)
- **Error Messages:** "Name must contain only letters and spaces (max 50 characters)"
- **Dependencies:** None

### Adult(s) Above 12 Years Field
- **Type:** Number
- **Required:** Y
- **Validations:** 
  - Min: 1
  - Max: 99
  - Integer only
- **Valid Examples:** 
  - 1, 2, 5, 10
- **Invalid Examples:**
  - 0 (below minimum)
  - 100 (exceeds maximum)
  - 1.5 (decimal)
  - -1 (negative)
- **Error Messages:** "At least 1 adult is required"
- **Dependencies:** None

### Children (Ages 0-12) Field
- **Type:** Number
- **Required:** Y
- **Validations:** 
  - Min: 0
  - Max: 99
  - Integer only
- **Valid Examples:** 
  - 0, 1, 2, 5
- **Invalid Examples:**
  - 100 (exceeds maximum)
  - 1.5 (decimal)
  - -1 (negative)
- **Error Messages:** "Children count must be between 0 and 99"
- **Dependencies:** None

### Household Staff/Pets Fields
- **Type:** Radio + Conditional Number
- **Required:** Y (Radio); Conditional (Number)
- **Validations:** 
  - Radio: Yes/No
  - If Yes: Number field Min: 1, Max: 99
- **Valid Examples:** 
  - No (no number required)
  - Yes + 1, 2, 5
- **Invalid Examples:**
  - Yes + 0 (if Yes selected, must be ≥1)
  - Yes + 100 (exceeds max)
- **Error Messages:** "Please specify the number of household staff/pets"
- **Dependencies:** Radio selection → Number field visibility

### People of Determination Field
- **Type:** Radio + Conditional Text Area
- **Required:** Y (Radio); Conditional (Text Area)
- **Validations:** 
  - Radio: Yes/No
  - If Yes: Text Area required, Max 500 characters
- **Valid Examples:** 
  - No (no text required)
  - Yes + "Need wheelchair assistance for elderly patient during move-in"
- **Invalid Examples:**
  - Yes + [empty text] (text required if Yes)
  - Yes + [501 characters] (exceeds max)
- **Error Messages:** "Please provide details about special requirements"
- **Dependencies:** Radio selection → Text Area visibility

### Tenancy Contract Number Field
- **Type:** Text
- **Required:** Y (for Tenant)
- **Validations:** Format: AB-12345678 (2 letters, hyphen, 8 digits)
- **Valid Examples:** 
  - AB-12345678
  - XY-98765432
- **Invalid Examples:**
  - AB12345678 (missing hyphen)
  - A-12345678 (only 1 letter)
  - AB-1234567 (only 7 digits)
- **Error Messages:** "Please enter a valid tenancy contract number"
- **Dependencies:** None

### Trade License Number Field
- **Type:** Text
- **Required:** Y (for HHO Company)
- **Validations:** 
  - Numeric only
  - Max 8 digits
- **Valid Examples:** 
  - 12345678
  - 1234567
- **Invalid Examples:**
  - AB123456 (contains letters)
  - 123456789 (exceeds 8 digits)
- **Error Messages:** "Trade license number must be numeric (max 8 digits)"
- **Dependencies:** Trade License Expiry Date

### Operator Office Number Field
- **Type:** Text
- **Required:** Y (for HHO Company)
- **Validations:** Format: +971 122345678 (country code + space + 9 digits)
- **Valid Examples:** 
  - +971 122345678
- **Invalid Examples:**
  - 971122345678 (missing +)
  - +971122345678 (missing space)
  - +971 12234567 (only 8 digits)
- **Error Messages:** "Please enter a valid office number"
- **Dependencies:** None

### File Upload Fields
- **Type:** File Upload
- **Required:** Y (varies by field)
- **Validations:** 
  - Supported formats: PDF, JPG, JPEG, PNG, GIF
  - Max file size: 2MB
- **Valid Examples:** 
  - document.pdf (1.5MB)
  - image.jpg (500KB)
- **Invalid Examples:**
  - document.docx (unsupported format)
  - image.jpg (3MB - exceeds limit)
- **Error Messages:** 
  - "Unsupported file format. Please upload PDF, JPG, JPEG, PNG, or GIF"
  - "File size exceeds 2MB limit"
- **Dependencies:** None

### Status Field (Master Data)
- **Type:** Radio
- **Required:** Y
- **Validations:** Active/Inactive only
- **Valid Examples:** 
  - Active
  - Inactive
- **Invalid Examples:** N/A (radio button)
- **Error Messages:** N/A
- **Dependencies:** Only one Active record per unique property combination

### Property Hierarchy Fields (Master Community/Community/Tower)
- **Type:** Dropdown (cascading)
- **Required:** Y (Master Community, Community); N (Tower)
- **Validations:** 
  - Master Community: From master data
  - Community: Filtered by selected Master Community
  - Tower: Filtered by selected Community
- **Valid Examples:** 
  - Sobha Hartland → Sobha Crest → Tower 1
- **Invalid Examples:** N/A (dropdown selection)
- **Error Messages:** "Please select a valid property"
- **Dependencies:** Master Community → Community → Tower (cascading)

### Move-out Date Field
- **Type:** Date Picker
- **Required:** Y
- **Validations:** 
  - Format: DD/MM/YYYY
  - Must be future date
  - Enabled only 30 days before tenancy end date
- **Valid Examples:** 
  - Any future date (if within 30-day window)
- **Invalid Examples:**
  - Past dates
  - Dates outside 30-day window
- **Error Messages:** "Move-out date must be in the future"
- **Dependencies:** Tenancy End Date (30-day rule)

### Actual Move-in/Move-out Date Field
- **Type:** Date Picker
- **Required:** Y (when closing request)
- **Validations:** 
  - Format: DD/MM/YYYY
  - Can be past, present, or future
- **Valid Examples:** 
  - 12/06/2025
  - Today's date
- **Invalid Examples:**
  - Invalid date format
- **Error Messages:** "Please enter the actual move-in/move-out date"
- **Dependencies:** Request Status = Approved

---

## 4. EDGE CASES & BOUNDARIES

### Numeric Fields (Adults, Children, Staff, Pets)
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| Minimum boundary | 0 (Children) | Valid |
| Below minimum | -1 | Error: "Value must be ≥ 0" |
| Minimum required | 1 (Adults) | Valid |
| Below minimum required | 0 (Adults) | Error: "At least 1 adult required" |
| Maximum boundary | 99 | Valid |
| Above maximum | 100 | Error: "Value must be ≤ 99" |
| Decimal value | 1.5 | Error: "Must be whole number" |
| Non-numeric | "abc" | Error: "Must be numeric" |
| Empty/Null | [empty] | Error: "Field is required" |

### Date Fields
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| Valid future date | 15/05/2026 | Valid |
| Today's date | [today] | Valid (for move-in) |
| Past date | 15/05/2023 | Error: "Date cannot be in past" |
| Invalid day | 32/05/2025 | Error: "Invalid date" |
| Invalid month | 15/13/2025 | Error: "Invalid date" |
| Invalid year | 15/05/1900 | Error: "Invalid date" |
| Wrong format | 2025-05-15 | Error: "Use DD/MM/YYYY format" |
| Empty/Null | [empty] | Error: "Field is required" |
| End before Start | Start: 15/05/2025, End: 14/05/2025 | Error: "End date must be after start date" |
| Same Start/End | Start: 15/05/2025, End: 15/05/2025 | Error: "End date must be after start date" |

### Text Fields (Names)
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| Valid name | "Mohammed" | Valid |
| Max length (50) | [50 characters] | Valid |
| Max length + 1 | [51 characters] | Error: "Max 50 characters" |
| Empty/Null | [empty] | Error: "Field is required" (if required) |
| Whitespace only | "   " | Error: "Field is required" |
| Leading/trailing spaces | " Mohammed " | Auto-trim or Valid |
| Numbers | "Mohammed123" | Error: "Letters only" |
| Special characters | "@Mohammed" | Error: "Letters only" |
| Multiple spaces | "Al  Maktoum" | Valid (or auto-normalize) |

### Email Fields
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| Valid email | essa.mohammed@gmail.com | Valid |
| Missing @ | essa.mohammedgmail.com | Error: "Invalid email" |
| Missing domain | essa.mohammed@ | Error: "Invalid email" |
| Missing local part | @gmail.com | Error: "Invalid email" |
| Multiple @ | essa@@gmail.com | Error: "Invalid email" |
| Spaces | "essa mohammed@gmail.com" | Error: "Invalid email" |
| Empty/Null | [empty] | Error: "Field is required" |
| Special chars in local | essa+mohammed@gmail.com | Valid |
| Multiple emails (comma-separated) | essa@gmail.com, admin@sobha.com | Valid (for Email Recipients field) |
| Multiple emails (no space) | essa@gmail.com,admin@sobha.com | Valid |
| Multiple emails (invalid one) | essa@gmail.com, invalid@ | Error: "Invalid email in list" |

### Mobile Number
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| Valid format | 0555089812 | Valid |
| Valid with space | 0555 089812 | Valid |
| Missing leading 0 | 555089812 | Error: "Invalid format" |
| Too short | 055508981 | Error: "Invalid format" |
| Too long | 05550898123 | Error: "Invalid format" |
| Contains letters | 0555ABC812 | Error: "Invalid format" |
| Empty/Null | [empty] | Error: "Field is required" |
| International format | +971555089812 | Error: "Use format: 0555 0898XX" |

### File Upload
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| Valid PDF (1MB) | document.pdf | Valid |
| Valid JPG (500KB) | image.jpg | Valid |
| Max size (2MB) | file.pdf (2MB) | Valid |
| Over max size | file.pdf (2.1MB) | Error: "Max 2MB" |
| Unsupported format | document.docx | Error: "Unsupported format" |
| Empty file | file.pdf (0KB) | Error: "File is empty" |
| No file selected | [empty] | Error: "File is required" |
| Multiple files | [2 files] | Error: "Select one file only" |
| Corrupted file | corrupted.pdf | Error: "File is corrupted" |

### Dropdown/Cascading Fields
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| Valid selection | Master Community → Community → Tower | Valid |
| No selection | [empty] | Error: "Field is required" |
| Parent changed | Change Master Community | Child dropdowns reset |
| Invalid combination | Community not under selected Master Community | Error: "Invalid selection" |
| Disabled child | Tower (when Community has no towers) | Dropdown disabled or empty |

### Radio + Conditional Fields
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| No selected | [empty] | Valid (if default = No) |
| Yes + valid number | Yes + 2 | Valid |
| Yes + no number | Yes + [empty] | Error: "Number required" |
| Yes + 0 | Yes + 0 | Error: "Must be ≥ 1" |
| No + number entered | No + 2 | Valid (number ignored) |

### Status Workflow Transitions
| Current Status | Action | Expected Result |
|----------------|--------|-----------------|
| New | Cancel | Status = Cancel |
| New | Edit | Form opens |
| New | Mark RFI | Status = RFI Submitted |
| New | Approve | Status = Approved |
| RFI Submitted | Cancel | Status = Cancel |
| RFI Submitted | Edit | Form opens |
| RFI Submitted | Approve | Status = Approved |
| Approved | Cancel | Error: "Cannot cancel approved request" |
| Approved | Close | Status = Closed (requires Actual Date) |
| Closed | Any action | Error: "Request is closed" |
| Cancel | Any action | Error: "Request is cancelled" |

### Unique Constraints
| Scenario | Input | Expected Result |
|----------|-------|-----------------|
| Duplicate Active MIP Template | Same Master Community/Community/Tower | Error: "Active template already exists" |
| Duplicate Inactive MIP Template | Same Master Community/Community/Tower | Valid |
| Duplicate Active Welcome Pack | Same Master Community/Community/Tower | Error: "Active welcome pack already exists" |
| Duplicate Active Email Config | Same Master Community/Community/Tower | Error: "Active email config already exists" |

### Move-out 30-Day Rule
| Scenario | Tenancy End Date | Current Date | Expected Result |
|----------|------------------|--------------|-----------------|
| Within 30 days | 15/06/2025 | 16/05/2025 | Move-out button enabled |
| Exactly 30 days | 15/06/2025 | 15/05/2025 | Move-out button enabled |
| 31 days before | 15/06/2025 | 14/05/2025 | Move-out button disabled |
| After end date | 15/06/2025 | 20/06/2025 | Move-out button enabled |

---

## 5. DATA CONSTRAINTS & FORMATS

### Date Formats
| Field | Format | Example |
|-------|--------|---------|
| All Date Fields | DD/MM/YYYY | 15/05/2025 |
| History Log Timestamps | DD MMM YYYY HH:MM AM/PM | 07 Apr 2025 02:22 PM |

### Email Patterns
| Field | Pattern | Example |
|-------|---------|---------|
| Single Email | standard email regex | essa.mohammed@gmail.com |
| Multiple Emails | comma-separated emails | essa@gmail.com, admin@sobha.com |

### Phone Number Formats
| Field | Format | Example |
|-------|--------|---------|
| Mobile Number | 0XXX XXXXXXX (10 digits) | 0555 089812 |
| Operator Office Number | +971 XXXXXXXXX | +971 122345678 |

### ID Number Formats
| Field | Format | Example |
|-------|--------|---------|
| Emirates ID | 784-XXXX-XXXXXXX-X | 784-1234-1234567-1 |
| Tenancy Contract Number | AA-XXXXXXXX | AB-12345678 |
| Unit Permit Number | AA-XXXXXXXX | AB-12345678 |
| Trade License Number | XXXXXXXX (max 8 digits) | 12345678 |

### Character Limits
| Field | Min | Max | Type |
|-------|-----|-----|------|
| First Name | 1 | 50 | Letters + spaces |
| Middle Name | 0 | 50 | Letters + spaces |
| Last Name | 1 | 50 | Letters + spaces |
| Company Name | 1 | 100 | Alphanumeric |
| Representative Name | 1 | 50 | Alphanumeric |
| People of Determination Details | 0 | 500 | Alphanumeric |
| Move-out Reason | 1 | 200 | Alphanumeric |
| History Comments | 0 | 1000 | Alphanumeric |

### File Upload Constraints
| Property | Value |
|----------|-------|
| Max File Size | 2MB |
| Allowed Formats | PDF, JPG, JPEG, PNG, GIF |
| Max Files per Field | 1 |

### Numeric Ranges
| Field | Min | Max |
|-------|-----|-----|
| Adults (Above 12 years) | 1 | 99 |
| Children (Ages 0-12) | 0 | 99 |
| Household Staff | 1 | 99 |
| Pets | 1 | 99 |

### Dropdown Values
| Field | Values |
|-------|--------|
| Status | Active, Inactive |
| Request Status (Move-in) | New, RFI Submitted, Approved, Closed, Cancel |
| Request Status (Move-out) | New, Approved, Moved-Out, Cancel |
| Request Status (Account Renewal) | New, RFI Submitted, Approved, Renewed, Cancel |
| Move-in Type | Owner, Tenant, HHO Unit, HHO Company |
| Residency Type | Owner, Tenant, HHO Unit, HHO Company |
| Move-out Reason | Job Relocation, Personal, Other |

---

## 6. INTEGRATION & SECURITY

### User Roles & Permissions
| Role | Permissions |
|------|-------------|
| Super Admin | All operations (Create, View, Edit, Approve, Cancel, Close) |
| Community Admin | View, Create, Edit, Approve, Cancel (limited to assigned communities) |
| Backoffice User | View only (MIP/MOP templates) |

### Authentication
- Login required for all operations
- Session management (timeout not specified)
- Username/Password authentication

### Authorization
| Feature | Super Admin | Community Admin |
|---------|-------------|-----------------|
| View MIP/MOP Template | ✓ | ✓ |
| Create/Edit Welcome Pack | ✓ | ✓ |
| Create/Edit Email Recipients | ✓ | ✗ |
| Create Move-in Request | ✓ | ✓ |
| Approve Move-in Request | ✓ | ✓ |
| Close Move-in Request | ✓ | ✓ |
| Create Move-out Request | ✓ | ✓ |
| Approve Move-out Request | ✓ | ✓ |
| Create Account Renewal | ✓ | ✓ |
| Approve Account Renewal | ✓ | ✓ |
| View Active Residents | ✓ | ✓ |

### Sensitive Data Fields
| Field | Sensitivity | Handling |
|-------|-------------|----------|
| Emirates ID Number | High | Masked display (784-xxxx-xxxxxxx-x) |
| Mobile Number | Medium | Masked display (0555 0898XX) |
| Email ID | Medium | Full display |
| Tenancy Contract Number | Medium | Full display |
| Trade License Number | Medium | Full display |
| Uploaded Documents | High | Secure storage, access-controlled |

### API Endpoints (Inferred)
| Operation | Method | Endpoint (Assumed) |
|-----------|--------|-------------------|
| Get MIP Template List | GET | /api/master-data/mip-templates |
| Get MOP Template List | GET | /api/master-data/mop-templates |
| Create Welcome Pack | POST | /api/master-data/welcome-packs |
| Update Welcome Pack | PUT | /api/master-data/welcome-packs/{id} |
| Create Email Recipients | POST | /api/master-data/email-recipients |
| Update Email Recipients | PUT | /api/master-data/email-recipients/{id} |
| Create Move-in Request | POST | /api/move-in/requests |
| Update Move-in Request | PUT | /api/move-in/requests/{id} |
| Approve Move-in Request | POST | /api/move-in/requests/{id}/approve |
| Close Move-in Request | POST | /api/move-in/requests/{id}/close |
| Cancel Move-in Request | POST | /api/move-in/requests/{id}/cancel |
| Get Move-in Request List | GET | /api/move-in/requests |
| Get Move-in Request Details | GET | /api/move-in/requests/{id} |
| Create Move-out Request | POST | /api/move-out/requests |
| Approve Move-out Request | POST | /api/move-out/requests/{id}/approve |
| Close Move-out Request | POST | /api/move-out/requests/{id}/close |
| Create Account Renewal | POST | /api/account-renewal/requests |
| Approve Account Renewal | POST | /api/account-renewal/requests/{id}/approve |
| Get Active Residents | GET | /api/active-residents |
| Get Residency History | GET | /api/active-residents/{id}/history |
| Get Asset Details | GET | /api/active-residents/{id}/assets |
| Upload Document | POST | /api/documents/upload |

### Request/Response Formats (Assumed)
**Content-Type:** application/json

**Example Move-in Request Creation:**
```json
{
  "moveInType": "Tenant",
  "masterCommunity": "Sobha Hartland",
  "community": "Sobha Crest",
  "tower": "Tower 1",
  "unitNumber": "A-123",
  "moveInDate": "2025-05-15",
  "userDetails": {
    "firstName": "Essa",
    "middleName": "Mohammed",
    "lastName": "Mohammed",
    "mobileNumber": "0555089812",
    "emailId": "essa.mohammed@gmail.com",
    "emiratesIdNumber": "784-1234-1234567-1",
    "emiratesIdExpiry": "2025-12-31",
    "tenancyContractNumber": "AB-12345678",
    "tenancyStartDate": "2025-05-15",
    "tenancyEndDate": "2026-05-14"
  },
  "moveInDetails": {
    "adults": 3,
    "children": 2,
    "householdStaff": 0,
    "pets": 2,
    "peopleOfDetermination": true,
    "determinationDetails": "Need wheelchair assistance"
  },
  "documents": {
    "emiratesIdFront": "base64_encoded_file",
    "emiratesIdBack": "base64_encoded_file",
    "ejari": "base64_encoded_file"
  }
}
```

**Example Response:**
```json
{
  "success": true,
  "requestId": "123459",
  "status": "New",
  "message": "Move-in request created successfully"
}
```

---

## 7. BUSINESS LOGIC & CALCULATIONS

### SLA Tracking
- **Logic:** Track time elapsed since request creation
- **Breached SLA:** When elapsed time > defined SLA threshold (not specified in docs)
- **Display:** Counter on dashboard and list view

### Status Workflow State Machine

**Move-in Request:**
```
New → [Cancel] → Cancel (terminal)
New → [Mark RFI] → RFI Submitted
New → [Approve] → Approved
RFI Submitted → [Cancel] → Cancel (terminal)
RFI Submitted → [Approve] → Approved
Approved → [Close] → Closed (terminal)
```

**Move-out Request:**
```
New → [Cancel] → Cancel (terminal)
New → [Approve] → Approved
Approved → [Close] → Moved-Out (terminal)
```

**Account Renewal Request:**
```
New → [Cancel] → Cancel (terminal)
New → [Mark RFI] → RFI Submitted
New → [Approve] → Renewed (terminal)
RFI Submitted → [Cancel] → Cancel (terminal)
RFI Submitted → [Approve] → Renewed (terminal)
```

### Move-out Eligibility Calculation
- **Formula:** `Current Date >= (Tenancy End Date - 30 days)`
- **Example:** 
  - Tenancy End Date: 15/06/2025
  - Eligible From: 16/05/2025
  - If Current Date = 16/05/2025 or later → Move-out button enabled

### Account Renewal Eligibility
- **Logic:** Only applicable for Tenant, HHO Unit, HHO Company
- **Owner:** Account Renewal option NOT available

### Unique Active Record Constraint
- **Logic:** For Master Data (MIP/MOP Template, Welcome Pack, Email Recipients)
- **Formula:** `COUNT(Active Records WHERE Master Community = X AND Community = Y AND Tower = Z) <= 1`
- **Enforcement:** On Save, check if another Active record exists for same property combination

### Cascading Dropdown Logic
- **Master Community Selection:**
  - Loads all Master Communities from master data
- **Community Selection:**
  - Filters Communities WHERE `Master Community ID = Selected Master Community`
- **Tower Selection:**
  - Filters Towers WHERE `Community ID = Selected Community`
- **Reset Logic:**
  - If Master Community changes → Reset Community and Tower
  - If Community changes → Reset Tower

### History Log Timestamp
- **Format:** DD MMM YYYY HH:MM AM/PM
- **Timezone:** Not specified (assume server timezone)
- **Events Logged:**
  - Request Created
  - Request Amended (on Edit)
  - Marked as RFI
  - Request Approved
  - Request Closed
  - Request Cancelled

### Dashboard Counter Calculations
- **New:** `COUNT(Requests WHERE Status = 'New')`
- **RFI Pending:** `COUNT(Requests WHERE Status = 'RFI Submitted')`
- **Breached SLA:** `COUNT(Requests WHERE SLA_Breached = true)`
- **Approved:** `COUNT(Requests WHERE Status = 'Approved')`
- **Closed:** `COUNT(Requests WHERE Status = 'Closed')`
- **Total:** `COUNT(All Requests)`

### Active Residents Counter Calculations
- **Owner:** `COUNT(Active Residents WHERE Residency Type = 'Owner')`
- **Tenant:** `COUNT(Active Residents WHERE Residency Type = 'Tenant')`
- **HHO:** `COUNT(Active Residents WHERE Residency Type = 'HHO Unit')`
- **HHC:** `COUNT(Active Residents WHERE Residency Type = 'HHO Company')`
- **Total:** `SUM(Owner + Tenant + HHO + HHC)`

### Conditional Field Visibility
| Parent Field | Parent Value | Child Field | Visibility |
|--------------|--------------|-------------|------------|
| Household staff(s) | Yes | Number of Staff | Visible |
| Household staff(s) | No | Number of Staff | Hidden |
| Pets(s) | Yes | Number of Pets | Visible |
| Pets(s) | No | Number of Pets | Hidden |
| People of determination | Yes | Details Text Area | Visible |
| People of determination | No | Details Text Area | Hidden |

### Document Requirements by Move-in Type
| Move-in Type | Required Documents |
|--------------|-------------------|
| Owner | None |
| Tenant | Emirates ID Front, Emirates ID Back, Ejari |
| HHO Unit | Unit Permit |
| HHO Company | Unit Permit, Emirates ID Front, Emirates ID Back, Company Trade License |

### Account Renewal Document Requirements
| Move-in Type | Required Documents |
|--------------|-------------------|
| Tenant | Ejari |
| HHO Unit | Dubai Tourism Unit Permit |
| HHO Company | DTCM, Emirates ID Front, Emirates ID Back, Company Trade License |

---

## 8. TEST DATA EXAMPLES

### Valid Test Data Sets

**Owner Move-in:**
```
Master Community: Sobha Hartland
Community: Sobha Crest
Tower: Tower 1
Unit: A-123
Move-in Date: 15/05/2025
First Name: Essa
Middle Name: Mohammed
Last Name: Mohammed
Mobile: 0555089812
Email: essa.mohammed@gmail.com
Adults: 3
Children: 2
Household Staff: No
Pets: Yes, 2
People of Determination: Yes, "Need wheelchair assistance"
```

**Tenant Move-in:**
```
[Same as Owner, plus:]
Emirates ID: 784-1234-1234567-1
Emirates ID Expiry: 31/12/2025
Tenancy Contract: AB-12345678
Tenancy Start: 15/05/2025
Tenancy End: 14/05/2026
Documents: Emirates ID Front, Back, Ejari
```

**HHO Unit Move-in:**
```
Master Community: Sobha Hartland
Community: Sobha Crest
Tower: Tower 1
Unit: A-123
Move-in Date: 15/05/2025
First Name: Essa
Last Name: Mohammed
Mobile: 0555089812
Email: essa.mohammed@gmail.com
Unit Permit: AB-12345678
Permit Start: 15/05/2025
Permit End: 14/05/2026
Document: Unit Permit
```

**HHO Company Move-in:**
```
[Same as HHO Unit, plus:]
Representative: Essa
Company: ABC Company
Company Email: abccompany@gmail.com
Office Number: +971 122345678
Trade License: 12345678
Trade License Expiry: 31/12/2025
Lease Start: 15/05/2025
Lease End: 14/05/2026
Nationality: United Arab Emirates
Emirates ID: 12345678
Emirates ID Expiry: 31/12/2025
Documents: Unit Permit, Emirates ID Front, Back, Trade License
```

### Invalid Test Data Sets

**Invalid Email:**
```
essa.mohammed@ (missing domain)
@gmail.com (missing local part)
essa mohammed@gmail.com (contains space)
```

**Invalid Mobile:**
```
555089812 (missing leading 0)
055508981 (too short)
0555ABC812 (contains letters)
```

**Invalid Dates:**
```
32/05/2025 (invalid day)
15/13/2025 (invalid month)
15/05/2023 (past date for move-in)
```

**Invalid Emirates ID:**
```
784123412345671 (no dashes)
784-123-123456-1 (wrong format)
```

**Invalid Numeric Fields:**
```
Adults: 0 (below minimum)
Children: 100 (exceeds maximum)
Adults: 1.5 (decimal not allowed)
```

---

## 9. ERROR MESSAGES CATALOG

| Field/Scenario | Error Message |
|----------------|---------------|
| Required field empty | "Field is required" |
| Invalid email | "Please enter a valid email address" |
| Invalid mobile | "Please enter a valid mobile number" |
| Invalid Emirates ID | "Please enter a valid Emirates ID number" |
| Invalid date format | "Please enter a valid date in DD/MM/YYYY format" |
| Past move-in date | "Move-in date cannot be in the past" |
| End date before start | "Tenancy end date must be after start date" |
| Emirates ID expired | "Emirates ID expiry date must be in the future" |
| Name with numbers | "Name must contain only letters and spaces (max 50 characters)" |
| Adults below minimum | "At least 1 adult is required" |
| Number exceeds max | "Value must be ≤ 99" |
| Decimal in integer field | "Must be whole number" |
| File size exceeded | "File size exceeds 2MB limit" |
| Unsupported file format | "Unsupported file format. Please upload PDF, JPG, JPEG, PNG, or GIF" |
| Duplicate active record | "Active [template/welcome pack/email config] already exists for this property" |
| Invalid status transition | "Cannot [action] request in [current status] status" |
| Move-out not eligible | "Move-out option will be enabled 30 days before tenancy end date" |
| Account renewal not applicable | "Account renewal is not applicable for Owner type" |

---

## 10. ACCEPTANCE CRITERIA SUMMARY

### UC-125: View MIP/MOP Template
- ✓ Super Admin and Community Admin can view templates
- ✓ Templates displayed in list view with property hierarchy
- ✓ Search and filter functionality works
- ✓ Only one active template per unique property combination
- ✓ History log shows all transactions

### UC-126: Welcome Pack Setup
- ✓ Super Admin and Community Admin can create/edit
- ✓ File upload validates format and size
- ✓ Only one active welcome pack per unique property combination
- ✓ Status toggle works (Active/Inactive)
- ✓ History log shows all transactions

### UC-127: Email Recipients Setup
- ✓ Super Admin only can configure
- ✓ Multiple emails accepted (comma-separated)
- ✓ Email validation works
- ✓ Only one active configuration per unique property combination
- ✓ History log shows all transactions

### UC-128: Move-in Request Management
- ✓ All 4 move-in types supported (Owner, Tenant, HHO Unit, HHO Company)
- ✓ Multi-step forms work correctly
- ✓ Field validations work as specified
- ✓ Document upload works for required types
- ✓ Status workflow transitions correctly
- ✓ SLA tracking and breach detection works
- ✓ Admin can approve/cancel/close requests
- ✓ History log captures all actions
- ✓ Dashboard counters update correctly

### Move-out Request Management
- ✓ Move-out option enabled 30 days before tenancy end
- ✓ Acknowledgment checkbox required
- ✓ Admin can approve/close requests
- ✓ Actual move-out date captured on closure
- ✓ Cancel with notification option works
- ✓ Status workflow transitions correctly

### Account Renewal Request Management
- ✓ Only applicable for Tenant, HHO Unit, HHO Company
- ✓ Owner type does not have renewal option
- ✓ Document upload works for required types
- ✓ Status workflow transitions correctly
- ✓ Admin can approve/cancel requests
- ✓ History log captures all actions

### Active Residents
- ✓ List view shows all active residents
- ✓ Residency history displayed correctly
- ✓ Asset details (access card, parking) displayed
- ✓ Counters by residency type work correctly
- ✓ Filter and search functionality works

---

**END OF STRUCTURED EXTRACTION**