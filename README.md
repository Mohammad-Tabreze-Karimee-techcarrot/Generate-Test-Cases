# 🤖 Two-Stage AI Test Case Generation System

An intelligent, automated test case generation system that leverages **Claude AI** for requirements analysis and **OpenAI GPT-4** for comprehensive test case creation.

## 🌟 Features

- **Two-Stage AI Pipeline**
  - Stage 1: Claude analyzes BRD & Figma PDFs and extracts structured requirements
  - Stage 2: OpenAI generates detailed test cases based on Claude's analysis

- **Smart Processing**
  - ✅ Automatic content chunking for large documents
  - ✅ Intelligent caching to avoid redundant API calls
  - ✅ Exponential backoff retry logic for API failures
  - ✅ Comprehensive error handling and logging

- **Output Quality**
  - 📊 Structured requirements analysis
  - ✅ Detailed test cases in markdown table format
  - 📝 Specific test data examples (not generic)
  - 🎯 Coverage for functional, negative, edge, UI, integration, and security scenarios

- **GitHub Actions Integration**
  - 🔄 Automatic generation on BRD/Figma updates
  - 📦 Dependency caching for faster runs
  - 📈 Summary reports in GitHub Actions
  - 🚀 Manual trigger with options

## 📁 Project Structure

```
.
├── generate_testcases.py          # Main script
├── config.py                       # Configuration settings
├── utils.py                        # Helper utilities
├── requirements.txt                # Python dependencies
├── .env                           # API keys (not committed)
├── .env.example                   # Environment template
├── testcase_generation.log        # Execution logs
├── .github/
│   └── workflows/
│       └── testcase-generation.yml
└── projects/
    └── [ProjectName]/
        ├── input/
        │   ├── BRD/                # Place BRD files here (.docx, .pdf)
        │   └── Figma/              # Place Figma exports here (.pdf)
        └── output/
            ├── analysis/           # Claude's analysis outputs
            ├── testcases/          # OpenAI's test cases
            └── cache/              # Cached results
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd <your-repo>

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API keys
nano .env
```

Add your API keys to `.env`:
```bash
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

Get API keys from:
- Anthropic: https://console.anthropic.com/
- OpenAI: https://platform.openai.com/api-keys

### 3. Organize Your Files

```bash
# Create project structure
mkdir -p projects/MyProject/input/BRD
mkdir -p projects/MyProject/input/Figma

# Add your documents
cp /path/to/requirements.docx projects/MyProject/input/BRD/
cp /path/to/figma_design.pdf projects/MyProject/input/Figma/
```

### 4. Run Locally

```bash
python generate_testcases.py
```

### 5. View Results

Check the output folders:
```bash
# View analysis
cat projects/MyProject/output/analysis/*_Analysis_Claude_*.md

# View test cases
cat projects/MyProject/output/testcases/*_TestCases_OpenAI_*.md

# View logs
cat testcase_generation.log
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# AI Model Settings
CLAUDE_CONFIG = {
    "model": "claude-sonnet-4-5-20250929",
    "max_tokens": 16000,
    "temperature": 0.2,
}

OPENAI_CONFIG = {
    "model": "gpt-4-turbo-preview",
    "max_tokens": 8000,
    "temperature": 0.3,
}

# Enable/disable caching
CACHE_CONFIG = {
    "enable_caching": True,
}

# Chunking for large documents
CONTENT_CONFIG = {
    "chunk_size": 50000,  # characters
}
```

## 🔧 GitHub Actions Setup

### 1. Add Repository Secrets

Go to: **Settings → Secrets and variables → Actions → New repository secret**

Add:
- `ANTHROPIC_API_KEY`: Your Claude API key
- `OPENAI_API_KEY`: Your OpenAI API key

### 2. Workflow Triggers

The workflow runs automatically when:
- BRD files are added/updated in `projects/**/input/BRD/`
- Figma files are added/updated in `projects/**/input/Figma/`
- The script is modified

### 3. Manual Trigger

Go to: **Actions → Two-Stage AI Test Case Generation → Run workflow**

Options:
- **Clear cache before running**: Remove all cached analyses
- **Process specific project only**: Enter project name (leave empty for all)

## 📊 Utility Scripts

### Generate Statistics Report

```bash
python utils.py projects/
```

### Clean Old Files (30+ days)

```python
from utils import clean_old_files
clean_old_files("projects", days_old=30)
```

### Compare Test Case Versions

```python
from utils import compare_versions
compare_versions("projects", "LoginModule")
```

### Export to Excel

```bash
# Install openpyxl first
pip install openpyxl

# Export
python -c "from utils import export_to_excel; export_to_excel('projects/MyProject/output/testcases/Module_TestCases_OpenAI_v20241015_1200.md', 'testcases.xlsx')"
```

## 🎯 Features in Detail

### Intelligent Caching

The system caches both Claude's analysis and OpenAI's test cases based on content hash. If the input documents haven't changed, cached results are used instantly.

```bash
# Clear cache for fresh generation
find projects -type d -name "cache" -exec rm -rf {} +
```

### Retry Logic

Automatic retry with exponential backoff for:
- Rate limit errors
- API timeouts
- Network issues

### Content Chunking

Large documents are automatically split into manageable chunks:
- Default: 50,000 characters per chunk
- Claude analyzes each chunk separately
- Results are combined seamlessly

### Comprehensive Logging

All operations are logged to `testcase_generation.log`:
```bash
# View recent logs
tail -f testcase_generation.log

# Search for errors
grep "ERROR" testcase_generation.log
```

## 📈 Expected Output

### Claude's Analysis Output

```markdown
# Requirements Analysis by Claude AI

**Project:** MyProject
**Module:** LoginModule

## 1. FUNCTIONAL REQUIREMENTS
- FR-001: User authentication with email/password
- FR-002: "Remember me" functionality
- FR-003: Password reset via email

## 2. UI COMPONENTS & FLOWS
| Field Name | Type | Required | Validation Rules | Default Value |
|------------|------|----------|------------------|---------------|
| Email | text | Y | Email format, max 100 chars | - |
| Password | password | Y | Min 8 chars, 1 uppercase, 1 number | - |

## 3. VALIDATION RULES
**Field: Email**
- Type: text
- Required: Y
- Validations: Valid email format, max 100 characters
- Valid Examples: user@example.com, test.user@company.co.uk
- Invalid Examples: invalid-email, @example.com, user@
- Error Messages: "Please enter a valid email address"

...
```

### OpenAI's Test Cases Output

```markdown
# Test Cases Generated by OpenAI

| Test Case ID | Module | Test Scenario | Test Type | Preconditions | Test Steps | Test Data | Expected Result | Priority |
|--------------|--------|---------------|-----------|---------------|------------|-----------|-----------------|----------|
| TC001 | Login | Valid login with correct credentials | Functional | User registered | 1. Navigate to login<br>2. Enter email<br>3. Enter password<br>4. Click Login | Email: john.doe@example.com<br>Password: Test@123 | User logged in successfully | High |
| TC002 | Login | Login with invalid email format | Negative | - | 1. Navigate to login<br>2. Enter invalid email<br>3. Click Login | Email: invalid-email<br>Password: Test@123 | Error: "Please enter a valid email" | High |
...
```

## 🐛 Troubleshooting

### Issue: "API key not found"
**Solution:** Check your `.env` file and ensure keys are set correctly.

### Issue: "Rate limit exceeded"
**Solution:** The script will automatically retry. Wait a few minutes or check your API usage.

### Issue: "No BRD files found"
**Solution:** Ensure BRD files are in `projects/[ProjectName]/input/BRD/`

### Issue: "Cache not working"
**Solution:** Check `config.py` and ensure `enable_caching: True`

### Issue: "Generated test cases seem incomplete"
**Solution:** 
- Increase `max_tokens` in config.py
- Check if BRD content is clear and detailed
- Review Claude's analysis for completeness

## 📝 Best Practices

1. **BRD Quality**: Provide detailed, well-structured BRD documents
2. **Figma Files**: Include all relevant screens and flows
3. **File Naming**: Use descriptive names for BRD files (becomes module name)
4. **Review Output**: Always review generated test cases for accuracy
5. **Version Control**: Keep old versions for comparison
6. **Cache Management**: Clear cache when requirements change significantly

## 🔒 Security

- Never commit `.env` file or API keys
- Use GitHub Secrets for Actions
- Regularly rotate API keys
- Review generated content before sharing externally

## 📚 Resources

- [Claude API Documentation](https://docs.anthropic.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional output formats (Excel, JSON, CSV)
- Integration with test management tools (Jira, TestRail)
- Support for more document formats
- UI dashboard for results

## 📄 License

[Your License Here]

## 💬 Support

For issues or questions:
1. Check the logs: `testcase_generation.log`
2. Review this README
3. Open an issue on GitHub

---

**Happy Testing! 🚀**