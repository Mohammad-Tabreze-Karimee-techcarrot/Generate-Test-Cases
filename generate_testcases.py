import os
from datetime import datetime
from docx import Document
from dotenv import load_dotenv
from anthropic import Anthropic
from openai import OpenAI
import fitz  # from PyMuPDF
import json

# --- Load environment variables ---
load_dotenv()
claude_api_key = os.getenv("ANTHROPIC_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not claude_api_key:
    raise ValueError("❌ Please set your ANTHROPIC_API_KEY in .env file")
if not openai_api_key:
    raise ValueError("❌ Please set your OPENAI_API_KEY in .env file")

claude_client = Anthropic(api_key=claude_api_key)
openai_client = OpenAI(api_key=openai_api_key)

# --- Define core paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECTS_DIR = os.path.join(BASE_DIR, "projects")

# --- Helper: Read BRD content ---
def read_brd_text(file_path):
    """
    Reads text from .docx or .pdf files.
    Returns a clean text string for AI processing.
    """
    try:
        if file_path.lower().endswith(".docx"):
            doc = Document(file_path)
            text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        elif file_path.lower().endswith(".pdf"):
            text = ""
            with fitz.open(file_path) as pdf_doc:
                for page in pdf_doc:
                    text += page.get_text("text")
        else:
            print(f"⚠️ Unsupported file type: {file_path}")
            return ""
        return text.strip()
    except Exception as e:
        print(f"⚠️ Error reading {file_path}: {e}")
        return ""

# --- Helper: Read Figma PDF ---
def read_figma_pdf(figma_dir):
    """
    Reads all Figma PDFs from the directory.
    Returns combined text content.
    """
    if not os.path.exists(figma_dir):
        return ""
    
    figma_content = ""
    for file in os.listdir(figma_dir):
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(figma_dir, file)
            print(f"📐 Reading Figma file: {file}")
            figma_content += f"\n\n=== FIGMA FILE: {file} ===\n\n"
            figma_content += read_brd_text(file_path)
    
    return figma_content.strip()

# --- STAGE 1: Claude Analysis ---
def analyze_with_claude(brd_content, figma_content, project_name, module_name):
    """
    Stage 1: Use Claude to analyze BRD and Figma PDFs.
    Extracts structured information about requirements, UI elements, flows, validations.
    """
    print("\n🔍 STAGE 1: Claude analyzing documents...")
    
    analysis_prompt = f"""
You are a senior Business Analyst and QA Architect. Analyze the following documents and extract structured information for test case generation.

Project: {project_name}
Module: {module_name}

=== BUSINESS REQUIREMENT DOCUMENT ===
{brd_content}

{"=== FIGMA DESIGN SPECIFICATIONS ===" if figma_content else ""}
{figma_content if figma_content else ""}

Your task is to analyze these documents and provide a DETAILED STRUCTURED ANALYSIS covering:

## 1. FUNCTIONAL REQUIREMENTS
- List all functional requirements with clear descriptions
- Identify business rules and logic
- Note any workflows or process flows
- Highlight integration points

## 2. UI/UX ELEMENTS (from Figma if available)
- List all UI components (buttons, fields, dropdowns, etc.)
- Identify navigation flows
- Note any interactive elements
- Describe layouts and screens

## 3. FIELD-LEVEL SPECIFICATIONS
For each input field, extract:
- Field name and type (text, number, date, etc.)
- Validation rules (required/optional, min/max length, format, regex)
- Default values
- Error messages
- Dependencies on other fields

## 4. EDGE CASES & BOUNDARIES
- Identify boundary conditions
- List potential edge cases
- Note error scenarios
- Identify negative test scenarios

## 5. DATA SPECIFICATIONS
- Sample valid data
- Sample invalid data
- Data constraints and formats
- Special characters handling

## 6. SECURITY & PERMISSIONS
- Access control requirements
- Authentication/Authorization needs
- Sensitive data handling

## 7. INTEGRATION POINTS
- External systems/APIs
- Data flow between modules
- Dependencies

Provide a comprehensive, well-structured analysis that will be used to generate detailed test cases.
Use clear headings, bullet points, and be specific with examples.
"""

    try:
        print("🔄 Claude analyzing documents...")
        response = claude_client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=8000,
            temperature=0.2,
            messages=[{"role": "user", "content": analysis_prompt}]
        )
        analysis = response.content[0].text.strip()
        print("✅ Claude analysis complete!")
        return analysis
    except Exception as e:
        print(f"❌ Claude analysis failed: {e}")
        # Fallback to simpler analysis
        return f"## Document Summary\n\nBRD Content:\n{brd_content[:2000]}...\n\nFigma Content:\n{figma_content[:1000] if figma_content else 'No Figma designs provided'}"

# --- STAGE 2: OpenAI Test Case Generation ---
def generate_testcases_with_openai(claude_analysis, project_name, module_name):
    """
    Stage 2: Use OpenAI to generate detailed test cases based on Claude's analysis.
    """
    print("\n📝 STAGE 2: OpenAI generating test cases...")
    
    testcase_prompt = f"""
You are an expert QA Engineer specializing in comprehensive test case design.

You have been provided with a detailed analysis of requirements and design specifications for:
Project: {project_name}
Module: {module_name}

=== ANALYSIS FROM REQUIREMENTS & DESIGN DOCUMENTS ===
{claude_analysis}

Based on this analysis, generate COMPREHENSIVE, DETAILED MANUAL TEST CASES covering ALL scenarios.

## Test Case Requirements:

### Coverage Areas:
1. **Functional Test Cases** - All positive scenarios (happy path)
2. **Negative Test Cases** - Error handling, invalid inputs
3. **Edge Cases** - Boundary conditions, limits
4. **Field Validation Test Cases** - Every field with all validation rules
5. **UI/UX Test Cases** - All UI elements, navigation, layouts
6. **Integration Test Cases** - Data flow, API calls, system interactions
7. **Security Test Cases** - Authentication, authorization, data protection
8. **Performance Considerations** - Load scenarios if mentioned

### Test Case Format - Markdown Table:
| Test Case ID | Module | Test Scenario | Test Type | Preconditions | Test Steps | Test Data | Expected Result | Priority |

### Test Case Guidelines:
- **Test Case ID**: Sequential numbering (TC001, TC002, etc.)
- **Module**: Specific module/feature name
- **Test Scenario**: Clear, descriptive scenario name
- **Test Type**: Functional/Negative/Edge/UI/Integration/Security
- **Preconditions**: What must be set up before testing
- **Test Steps**: Numbered, detailed steps (Step 1:, Step 2:, etc.)
- **Test Data**: SPECIFIC examples (not generic like "valid email" - use "john.doe@example.com")
- **Expected Result**: Clear, measurable expected outcome
- **Priority**: High/Medium/Low

### Important:
- Be SPECIFIC with test data (provide actual examples)
- Cover EVERY field mentioned in the analysis
- Include BOTH valid and invalid data for each field
- Test ALL validation rules explicitly
- Include boundary values (min-1, min, min+1, max-1, max, max+1)
- Test special characters, empty values, null values
- Be thorough - aim for 100+ test cases for comprehensive coverage

Generate the test cases now in a well-formatted markdown table.
"""

    try:
        print("🔄 OpenAI generating test cases...")
        response = openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": testcase_prompt}],
            max_tokens=8000,
            temperature=0.3
        )
        test_cases = response.choices[0].message.content.strip()
        print("✅ OpenAI test case generation complete!")
        return test_cases
    except Exception as e:
        print(f"❌ OpenAI generation failed: {e}")
        return f"Error generating test cases: {str(e)}"

# --- Helper: Save outputs ---
def save_analysis(project_name, module_name, analysis_content):
    """Save Claude's analysis for reference."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_dir = os.path.join(PROJECTS_DIR, project_name, "output", "analysis")
    os.makedirs(output_dir, exist_ok=True)

    file_name = f"{module_name}_Analysis_Claude_v{timestamp}.md"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# Requirements Analysis by Claude AI\n\n")
        f.write(f"**Project:** {project_name}\n")
        f.write(f"**Module:** {module_name}\n")
        f.write(f"**Analyzed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write(analysis_content)

    print(f"✅ Analysis saved to: {file_path}")

def save_testcases(project_name, module_name, testcases_content):
    """Save OpenAI's test cases."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_dir = os.path.join(PROJECTS_DIR, project_name, "output", "testcases")
    os.makedirs(output_dir, exist_ok=True)

    file_name = f"{module_name}_TestCases_OpenAI_v{timestamp}.md"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# Test Cases Generated by OpenAI\n")
        f.write(f"*(Based on Claude's Requirements Analysis)*\n\n")
        f.write(f"**Project:** {project_name}\n")
        f.write(f"**Module:** {module_name}\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write(testcases_content)

    print(f"✅ Test cases saved to: {file_path}")

# --- MAIN FUNCTION ---
def process_all_projects():
    print("🚀 Starting TWO-STAGE AI Test Case Generation...")
    print("📌 Stage 1: Claude (Analysis) → Stage 2: OpenAI (Test Cases)\n")

    projects_found = False
    for project_name in os.listdir(PROJECTS_DIR):
        project_path = os.path.join(PROJECTS_DIR, project_name)
        
        # Skip if not a directory
        if not os.path.isdir(project_path):
            continue
            
        brd_dir = os.path.join(project_path, "input", "BRD")
        figma_dir = os.path.join(project_path, "input", "Figma")

        if not os.path.exists(brd_dir):
            print(f"⚠️ No BRD directory found for project: {project_name}")
            continue

        projects_found = True
        
        # Process each BRD file
        for brd_file in os.listdir(brd_dir):
            if brd_file.lower().endswith((".docx", ".pdf")):
                brd_path = os.path.join(brd_dir, brd_file)
                module_name = os.path.splitext(brd_file)[0]
                
                print(f"\n{'='*60}")
                print(f"🧠 Processing: {project_name} → {module_name}")
                print(f"{'='*60}")

                # Read BRD
                print("📄 Reading BRD document...")
                brd_content = read_brd_text(brd_path)
                if not brd_content:
                    print(f"⚠️ Skipping {module_name} — empty or unreadable BRD")
                    continue

                # Read Figma PDFs if available
                figma_content = read_figma_pdf(figma_dir)
                if figma_content:
                    print(f"✅ Figma designs found and loaded")
                else:
                    print(f"ℹ️ No Figma designs found (optional)")

                # STAGE 1: Claude analyzes documents
                claude_analysis = analyze_with_claude(
                    brd_content, 
                    figma_content, 
                    project_name, 
                    module_name
                )
                save_analysis(project_name, module_name, claude_analysis)

                # STAGE 2: OpenAI generates test cases based on Claude's analysis
                test_cases = generate_testcases_with_openai(
                    claude_analysis,
                    project_name,
                    module_name
                )
                save_testcases(project_name, module_name, test_cases)

                print(f"\n✅ Completed: {project_name} → {module_name}")

    if not projects_found:
        print("⚠️ No projects with BRD files found in the projects directory")
    else:
        print("\n" + "="*60)
        print("🎉 All projects processed successfully!")
        print("📂 Check output/analysis/ for Claude's analysis")
        print("📂 Check output/testcases/ for OpenAI's test cases")
        print("="*60)

# --- Run the workflow ---
if __name__ == "__main__":
    process_all_projects()