import os
from datetime import datetime
from docx import Document
from dotenv import load_dotenv
from anthropic import Anthropic
import fitz  # from PyMuPDF

# --- Load environment variables ---
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("❌ Please set your ANTHROPIC_API_KEY in .env file")

client = Anthropic(api_key=api_key)

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

# --- Helper: Load prompt ---
def load_prompt():
    """Returns the embedded default prompt."""
    return """
You are a senior QA engineer with extensive experience in test case design.

Generate comprehensive MANUAL test cases based on the BRD covering:

1. Functional Scenarios (Happy Path)
2. Negative Scenarios (Error Handling)
3. Edge Cases and Boundary Conditions
4. UI/UX Validations
5. Field-Level Validations (data type, length, format, mandatory/optional)
6. Integration Points
7. Security Considerations (if applicable)

Output Format - Markdown Table:
| Test Case ID | Module | Test Scenario | Preconditions | Test Steps | Expected Result | Test Data | Priority | Type |

Requirements:
- Clear and executable test cases
- Specific test data examples
- Both valid and invalid scenarios
- Numbered sequentially (TC001, TC002...)
- Priority: High/Medium/Low
- Type: Functional/UI/Negative/Edge/Integration

Be thorough, specific, and production-ready.
"""

# --- AI call using Claude with model fallback ---
def generate_testcases(brd_content, prompt_template, project_name, module_name):
    prompt = f"""
You are a senior QA engineer.

{prompt_template}

Project: {project_name}
Module: {module_name}

Below is the Business Requirement Document content:
{brd_content}

Generate detailed MANUAL TEST CASES as a Markdown table covering functional, UI, edge, and negative scenarios.
"""
    # Use a fallback model list for reliability
    models_to_try = ["claude-sonnet-4-5-20250929", "claude-sonnet-4-20250514", "claude-3-5-sonnet-20241022"]
    
    for model_name in models_to_try:
        try:
            print(f"🔄 Trying model: {model_name}")
            response = client.messages.create(
                model=model_name,
                max_tokens=4000,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}]
            )
            print(f"✅ Successfully used model: {model_name}")
            return response.content[0].text.strip()
        except Exception as e:
            print(f"⚠️ Model {model_name} failed: {e}")
            continue  # try next model

    print("❌ All models failed. Please check your API key or available Claude models.")
    return "Error while generating test cases."

# --- Helper: Save output ---
def save_output(project_name, module_name, output_content):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_dir = os.path.join(PROJECTS_DIR, project_name, "output", "testcases")
    os.makedirs(output_dir, exist_ok=True)

    file_name = f"{module_name}_TestCases_v{timestamp}.md"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Test cases saved to: {file_path}")

# --- MAIN FUNCTION ---
def process_all_projects():
    print("🚀 Starting test case generation...")
    prompt_template = load_prompt()

    projects_found = False
    for project_name in os.listdir(PROJECTS_DIR):
        project_path = os.path.join(PROJECTS_DIR, project_name)
        
        # Skip if not a directory
        if not os.path.isdir(project_path):
            continue
            
        brd_dir = os.path.join(project_path, "input", "BRD")

        if not os.path.exists(brd_dir):
            print(f"⚠️ No BRD directory found for project: {project_name}")
            continue

        projects_found = True
        for brd_file in os.listdir(brd_dir):
            if brd_file.lower().endswith((".docx", ".pdf")):
                brd_path = os.path.join(brd_dir, brd_file)
                module_name = os.path.splitext(brd_file)[0]
                print(f"\n🧠 Processing {project_name} → {module_name} ...")

                brd_content = read_brd_text(brd_path)
                if not brd_content:
                    print(f"⚠️ Skipping {module_name} — empty or unreadable BRD")
                    continue

                output = generate_testcases(brd_content, prompt_template, project_name, module_name)
                save_output(project_name, module_name, output)

    if not projects_found:
        print("⚠️ No projects with BRD files found in the projects directory")
    else:
        print("\n🎉 All projects processed successfully!")

# --- Run the workflow ---
if __name__ == "__main__":
    process_all_projects()