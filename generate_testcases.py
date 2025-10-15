import os
import json
import time
import hashlib
import logging
from datetime import datetime
from docx import Document
from dotenv import load_dotenv
from anthropic import Anthropic, APIError, RateLimitError
from openai import OpenAI
import fitz  # PyMuPDF

# --- Configure Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('testcase_generation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

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

# --- Configuration ---
CONFIG = {
    "claude_max_tokens": 16000,
    "openai_max_tokens": 8000,
    "claude_temperature": 0.2,
    "openai_temperature": 0.3,
    "max_retries": 3,
    "chunk_size": 50000,  # characters
    "enable_caching": True
}


# --- Helper: Content Hashing ---
def get_content_hash(*contents):
    """Generate MD5 hash of combined content for caching."""
    combined = "".join(str(c) for c in contents)
    return hashlib.md5(combined.encode()).hexdigest()


# --- Helper: Cache Management ---
def get_cache_path(project_name, module_name, cache_type="analysis"):
    """Get cache file path."""
    cache_dir = os.path.join(PROJECTS_DIR, project_name, "output", "cache")
    os.makedirs(cache_dir, exist_ok=True)
    return os.path.join(cache_dir, f"{module_name}_{cache_type}.json")


def load_from_cache(project_name, module_name, content_hash, cache_type="analysis"):
    """Load cached analysis if available and valid."""
    if not CONFIG["enable_caching"]:
        return None
    
    cache_file = get_cache_path(project_name, module_name, cache_type)
    
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
                
            if cache_data.get('content_hash') == content_hash:
                logger.info(f"✅ Cache hit for {module_name} ({cache_type})")
                return cache_data.get('content')
            else:
                logger.info(f"⚠️ Cache exists but content changed for {module_name}")
        except Exception as e:
            logger.warning(f"⚠️ Cache read error: {e}")
    
    return None


def save_to_cache(project_name, module_name, content_hash, content, cache_type="analysis"):
    """Save content to cache."""
    if not CONFIG["enable_caching"]:
        return
    
    cache_file = get_cache_path(project_name, module_name, cache_type)
    
    try:
        cache_data = {
            'content_hash': content_hash,
            'content': content,
            'timestamp': datetime.now().isoformat(),
            'cache_type': cache_type
        }
        
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, indent=2)
        
        logger.info(f"💾 Cached {cache_type} for {module_name}")
    except Exception as e:
        logger.warning(f"⚠️ Cache save error: {e}")


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
            logger.warning(f"⚠️ Unsupported file type: {file_path}")
            return ""
        
        cleaned_text = text.strip()
        logger.info(f"📄 Read {len(cleaned_text)} characters from {os.path.basename(file_path)}")
        return cleaned_text
    except Exception as e:
        logger.error(f"⚠️ Error reading {file_path}: {e}")
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
    figma_files = [f for f in os.listdir(figma_dir) if f.lower().endswith(".pdf")]
    
    if not figma_files:
        return ""
    
    logger.info(f"📐 Found {len(figma_files)} Figma file(s)")
    
    for file in figma_files:
        file_path = os.path.join(figma_dir, file)
        logger.info(f"📐 Reading Figma file: {file}")
        figma_content += f"\n\n=== FIGMA FILE: {file} ===\n\n"
        figma_content += read_brd_text(file_path)
    
    return figma_content.strip()


# --- Helper: Content Chunking ---
def chunk_content(text, max_chars=50000):
    """Split large documents into manageable chunks."""
    if len(text) <= max_chars:
        return [text]
    
    logger.info(f"📦 Chunking content: {len(text)} chars into ~{max_chars} char chunks")
    
    chunks = []
    paragraphs = text.split('\n\n')
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) + 2 <= max_chars:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    logger.info(f"✅ Created {len(chunks)} chunk(s)")
    return chunks


# --- Helper: Validate Analysis ---
def validate_analysis(analysis):
    """Ensure Claude's analysis contains required sections."""
    required_sections = [
        "FUNCTIONAL REQUIREMENTS",
        "UI",
        "VALIDATION",
        "EDGE CASES"
    ]
    
    analysis_upper = analysis.upper()
    missing = [s for s in required_sections if s not in analysis_upper]
    
    if missing:
        logger.warning(f"⚠️ Analysis may be incomplete. Missing: {missing}")
        return False
    
    if len(analysis) < 500:
        logger.warning(f"⚠️ Analysis seems too short: {len(analysis)} chars")
        return False
    
    logger.info("✅ Analysis validation passed")
    return True


# --- STAGE 1: Claude Analysis with Retry ---
def analyze_with_claude(brd_content, figma_content, project_name, module_name):
    """
    Stage 1: Use Claude to analyze BRD and Figma PDFs with retry logic.
    """
    logger.info("\n🔍 STAGE 1: Claude analyzing documents...")
    
    # Check cache first
    content_hash = get_content_hash(brd_content, figma_content)
    cached_analysis = load_from_cache(project_name, module_name, content_hash, "analysis")
    
    if cached_analysis:
        logger.info("📦 Using cached analysis")
        return cached_analysis
    
    # Chunk content if too large
    brd_chunks = chunk_content(brd_content, CONFIG["chunk_size"])
    
    if len(brd_chunks) > 1:
        logger.info(f"📦 Processing {len(brd_chunks)} BRD chunks separately")
        analyses = []
        for i, chunk in enumerate(brd_chunks):
            logger.info(f"🔄 Processing chunk {i+1}/{len(brd_chunks)}")
            chunk_analysis = _analyze_chunk_with_claude(
                chunk, 
                figma_content if i == 0 else "",  # Only include Figma in first chunk
                project_name, 
                module_name,
                chunk_num=i+1,
                total_chunks=len(brd_chunks)
            )
            analyses.append(chunk_analysis)
        
        # Combine analyses
        analysis = "\n\n---\n\n".join(analyses)
    else:
        analysis = _analyze_chunk_with_claude(
            brd_content, 
            figma_content, 
            project_name, 
            module_name
        )
    
    # Validate
    if not validate_analysis(analysis):
        logger.warning("⚠️ Analysis validation failed, but continuing...")
    
    # Cache the result
    save_to_cache(project_name, module_name, content_hash, analysis, "analysis")
    
    return analysis


def _analyze_chunk_with_claude(brd_content, figma_content, project_name, module_name, 
                                chunk_num=None, total_chunks=None):
    """Internal function to analyze a single chunk with retry logic."""
    
    chunk_info = f" (Chunk {chunk_num}/{total_chunks})" if chunk_num else ""
    
    analysis_prompt = f"""You are a senior Business Analyst and QA Architect. Analyze these documents and extract ONLY the essential structured information needed for test case generation{chunk_info}.

Project: {project_name}
Module: {module_name}

=== BUSINESS REQUIREMENT DOCUMENT ===
{brd_content}

{"=== FIGMA DESIGN SPECIFICATIONS ===" if figma_content else ""}
{figma_content if figma_content else ""}

Extract and structure the following in a CONCISE, SCANNABLE format:

## 1. FUNCTIONAL REQUIREMENTS
- List each requirement with ID and brief description
- Business rules (bullet points only)
- Critical workflows (high-level steps)

## 2. UI COMPONENTS & FLOWS
**Input Fields Table:**
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|

**Buttons/Actions:**
- Button name → Action/Behavior

**Navigation Flow:**
- Screen A → Action → Screen B

## 3. VALIDATION RULES (Critical for test cases)
For each field, provide in this format:

**Field: [name]**
- Type: [text/number/date/email/etc.]
- Required: [Y/N]
- Validations: [min/max length, format, regex patterns]
- Valid Examples: [actual data examples]
- Invalid Examples: [actual data examples]
- Error Messages: [exact error text]
- Dependencies: [related fields]

## 4. EDGE CASES & BOUNDARIES
- Boundary values (min-1, min, max, max+1)
- Null/empty field handling
- Special character scenarios
- Whitespace handling
- Dependent field combinations

## 5. DATA CONSTRAINTS & FORMATS
- Date formats (e.g., MM/DD/YYYY)
- Email patterns
- Phone number formats
- Character limits
- Allowed/disallowed characters

## 6. INTEGRATION & SECURITY
- API endpoints and methods
- Request/response formats
- Authentication requirements
- Authorization levels
- Sensitive data fields

## 7. BUSINESS LOGIC & CALCULATIONS
- Formula/calculations
- Conditional logic
- State transitions

Keep responses CONCISE and STRUCTURED. Use tables where possible. Focus on TESTABLE specifics with CONCRETE examples, not general descriptions."""

    for attempt in range(CONFIG["max_retries"]):
        try:
            logger.info(f"🔄 Claude analyzing{chunk_info}... (Attempt {attempt + 1}/{CONFIG['max_retries']})")
            
            response = claude_client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=CONFIG["claude_max_tokens"],
                temperature=CONFIG["claude_temperature"],
                messages=[{"role": "user", "content": analysis_prompt}]
            )
            
            analysis = response.content[0].text.strip()
            logger.info(f"✅ Claude analysis complete{chunk_info}! ({len(analysis)} chars)")
            return analysis
        
        except RateLimitError as e:
            wait_time = 2 ** attempt
            logger.warning(f"⚠️ Rate limit hit. Waiting {wait_time}s before retry...")
            time.sleep(wait_time)
        
        except APIError as e:
            logger.error(f"❌ Claude API Error (attempt {attempt + 1}): {e}")
            if attempt == CONFIG["max_retries"] - 1:
                logger.error("❌ All retry attempts exhausted")
                return f"## Analysis Failed\n\nError after {CONFIG['max_retries']} attempts: {str(e)}\n\nBRD Preview:\n{brd_content[:2000]}..."
            time.sleep(2 ** attempt)
        
        except Exception as e:
            logger.error(f"❌ Unexpected error: {e}")
            if attempt == CONFIG["max_retries"] - 1:
                return f"## Analysis Failed\n\nUnexpected error: {str(e)}"
            time.sleep(2 ** attempt)
    
    return "## Analysis Failed\n\nExhausted all retry attempts."


# --- STAGE 2: OpenAI Test Case Generation with Retry ---
def generate_testcases_with_openai(claude_analysis, project_name, module_name):
    """
    Stage 2: Use OpenAI to generate detailed test cases with retry logic.
    """
    logger.info("\n📝 STAGE 2: OpenAI generating test cases...")
    
    # Check cache
    content_hash = get_content_hash(claude_analysis)
    cached_testcases = load_from_cache(project_name, module_name, content_hash, "testcases")
    
    if cached_testcases:
        logger.info("📦 Using cached test cases")
        return cached_testcases
    
    testcase_prompt = f"""You are an expert QA Engineer specializing in comprehensive test case design.

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

### Test Case Format - Markdown Table:
| Test Case ID | Module | Test Scenario | Test Type | Preconditions | Test Steps | Test Data | Expected Result | Priority |

### Test Case Guidelines:
- **Test Case ID**: Sequential (TC001, TC002, etc.)
- **Module**: Specific module/feature name
- **Test Scenario**: Clear, descriptive scenario
- **Test Type**: Functional/Negative/Edge/UI/Integration/Security
- **Preconditions**: Setup required before testing
- **Test Steps**: Numbered, detailed steps (1., 2., 3., etc.)
- **Test Data**: SPECIFIC examples (use "john.doe@example.com" not "valid email")
- **Expected Result**: Clear, measurable outcome
- **Priority**: High/Medium/Low

### Critical Requirements:
- Be SPECIFIC with test data (provide actual examples)
- Cover EVERY field mentioned in the analysis
- Include BOTH valid and invalid data for each field
- Test ALL validation rules explicitly
- Include boundary values (min-1, min, min+1, max-1, max, max+1)
- Test special characters, empty values, null values
- Number test steps clearly (1. Do this, 2. Do that)
- Aim for 50-100+ test cases for comprehensive coverage

Generate the test cases now in a well-formatted markdown table."""

    for attempt in range(CONFIG["max_retries"]):
        try:
            logger.info(f"🔄 OpenAI generating test cases... (Attempt {attempt + 1}/{CONFIG['max_retries']})")
            
            response = openai_client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[{"role": "user", "content": testcase_prompt}],
                max_tokens=CONFIG["openai_max_tokens"],
                temperature=CONFIG["openai_temperature"]
            )
            
            test_cases = response.choices[0].message.content.strip()
            logger.info(f"✅ OpenAI test case generation complete! ({len(test_cases)} chars)")
            
            # Cache the result
            save_to_cache(project_name, module_name, content_hash, test_cases, "testcases")
            
            return test_cases
        
        except Exception as e:
            logger.error(f"❌ OpenAI Error (attempt {attempt + 1}): {e}")
            if attempt == CONFIG["max_retries"] - 1:
                logger.error("❌ All retry attempts exhausted")
                return f"## Test Case Generation Failed\n\nError after {CONFIG['max_retries']} attempts: {str(e)}"
            time.sleep(2 ** attempt)
    
    return "## Test Case Generation Failed\n\nExhausted all retry attempts."


# --- Helper: Save outputs ---
def save_analysis(project_name, module_name, analysis_content):
    """Save Claude's analysis for reference."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_dir = os.path.join(PROJECTS_DIR, project_name, "output", "analysis")
    os.makedirs(output_dir, exist_ok=True)
    
    file_name = f"{module_name}_Analysis_Claude_v{timestamp}.md"
    file_path = os.path.join(output_dir, file_name)
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Requirements Analysis by Claude AI\n\n")
            f.write(f"**Project:** {project_name}\n")
            f.write(f"**Module:** {module_name}\n")
            f.write(f"**Analyzed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")
            f.write(analysis_content)
        
        logger.info(f"✅ Analysis saved to: {file_path}")
    except Exception as e:
        logger.error(f"❌ Failed to save analysis: {e}")


def save_testcases(project_name, module_name, testcases_content):
    """Save OpenAI's test cases."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_dir = os.path.join(PROJECTS_DIR, project_name, "output", "testcases")
    os.makedirs(output_dir, exist_ok=True)
    
    file_name = f"{module_name}_TestCases_OpenAI_v{timestamp}.md"
    file_path = os.path.join(output_dir, file_name)
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Test Cases Generated by OpenAI\n")
            f.write(f"*(Based on Claude's Requirements Analysis)*\n\n")
            f.write(f"**Project:** {project_name}\n")
            f.write(f"**Module:** {module_name}\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")
            f.write(testcases_content)
        
        logger.info(f"✅ Test cases saved to: {file_path}")
    except Exception as e:
        logger.error(f"❌ Failed to save test cases: {e}")


# --- MAIN FUNCTION ---
def process_all_projects():
    """Main processing function for all projects."""
    logger.info("🚀 Starting TWO-STAGE AI Test Case Generation...")
    logger.info("📌 Stage 1: Claude (Analysis) → Stage 2: OpenAI (Test Cases)\n")
    
    projects_found = False
    total_processed = 0
    total_failed = 0
    
    for project_name in os.listdir(PROJECTS_DIR):
        project_path = os.path.join(PROJECTS_DIR, project_name)
        
        # Skip if not a directory
        if not os.path.isdir(project_path):
            continue
        
        brd_dir = os.path.join(project_path, "input", "BRD")
        figma_dir = os.path.join(project_path, "input", "Figma")
        
        if not os.path.exists(brd_dir):
            logger.warning(f"⚠️ No BRD directory found for project: {project_name}")
            continue
        
        projects_found = True
        
        # Process each BRD file
        for brd_file in os.listdir(brd_dir):
            if brd_file.lower().endswith((".docx", ".pdf")):
                brd_path = os.path.join(brd_dir, brd_file)
                module_name = os.path.splitext(brd_file)[0]
                
                logger.info(f"\n{'='*60}")
                logger.info(f"🧠 Processing: {project_name} → {module_name}")
                logger.info(f"{'='*60}")
                
                try:
                    # Read BRD
                    logger.info("📄 Reading BRD document...")
                    brd_content = read_brd_text(brd_path)
                    if not brd_content:
                        logger.warning(f"⚠️ Skipping {module_name} — empty or unreadable BRD")
                        total_failed += 1
                        continue
                    
                    # Read Figma PDFs if available
                    figma_content = read_figma_pdf(figma_dir)
                    if figma_content:
                        logger.info(f"✅ Figma designs found and loaded")
                    else:
                        logger.info(f"ℹ️ No Figma designs found (optional)")
                    
                    # STAGE 1: Claude analyzes documents
                    claude_analysis = analyze_with_claude(
                        brd_content,
                        figma_content,
                        project_name,
                        module_name
                    )
                    save_analysis(project_name, module_name, claude_analysis)
                    
                    # STAGE 2: OpenAI generates test cases
                    test_cases = generate_testcases_with_openai(
                        claude_analysis,
                        project_name,
                        module_name
                    )
                    save_testcases(project_name, module_name, test_cases)
                    
                    logger.info(f"\n✅ Completed: {project_name} → {module_name}")
                    total_processed += 1
                
                except Exception as e:
                    logger.error(f"❌ Failed to process {module_name}: {e}")
                    total_failed += 1
    
    if not projects_found:
        logger.warning("⚠️ No projects with BRD files found in the projects directory")
    else:
        logger.info("\n" + "="*60)
        logger.info("🎉 Processing Complete!")
        logger.info(f"✅ Successfully processed: {total_processed}")
        logger.info(f"❌ Failed: {total_failed}")
        logger.info("📂 Check output/analysis/ for Claude's analysis")
        logger.info("📂 Check output/testcases/ for OpenAI's test cases")
        logger.info("📂 Check testcase_generation.log for detailed logs")
        logger.info("="*60)


# --- Run the workflow ---
if __name__ == "__main__":
    try:
        process_all_projects()
    except KeyboardInterrupt:
        logger.info("\n⚠️ Process interrupted by user")
    except Exception as e:
        logger.error(f"\n❌ Fatal error: {e}")
        raise