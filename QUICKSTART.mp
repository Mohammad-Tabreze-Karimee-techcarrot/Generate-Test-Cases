# Quick Start Guide - 5 Minutes to Your First Test Cases

## Prerequisites

- Python 3.8+ installed
- API keys (Anthropic + OpenAI)
- Git (for GitHub setup)

## Step 1: Clone & Setup (2 minutes)

```bash
# Clone repository
git clone <your-repo-url>
cd <repo-directory>

# Run setup script
python setup.py

# This will:
# ✅ Check Python version
# ✅ Create .env file
# ✅ Install dependencies
# ✅ Create project folders
```

## Step 2: Add API Keys (1 minute)

```bash
# Edit .env file
nano .env

# Add your keys:
ANTHROPIC_API_KEY=sk-ant-xxxxx  # From https://console.anthropic.com
OPENAI_API_KEY=sk-xxxxx          # From https://platform.openai.com
```

## Step 3: Prepare Your Documents (1 minute)

```bash
# Copy your BRD to:
cp /path/to/requirements.docx projects/MyProject/input/BRD/

# Optional: Copy Figma export
cp /path/to/figma-export.pdf projects/MyProject/input/Figma/
```

## Step 4: Generate Test Cases (1 minute)

```bash
# Run locally
python generate_testcases.py

# Output will be in:
# - projects/MyProject/output/analysis/
# - projects/MyProject/output/testcases/
```

## Results

After running, you'll have:
- **Analysis file**: `*_Analysis_Claude_v*.md` - Claude's requirements breakdown
- **Test cases**: `*_TestCases_OpenAI_v*.md` - Detailed test cases in markdown table

## GitHub Actions (Optional)

1. Push code to GitHub
2. Go to Settings → Secrets → Add:
   - `ANTHROPIC_API_KEY`
   - `OPENAI_API_KEY`
3. On next push, workflow runs automatically

## Project Structure

```
projects/
└── MyProject/
    ├── input/
    │   ├── BRD/
    │   │   └── requirements.docx
    │   └── Figma/
    │       └── design.pdf
    └── output/
        ├── analysis/
        │   └── requirements_Analysis_Claude_v*.md
        ├── testcases/
        │   └── requirements_TestCases_OpenAI_v*.md
        └── cache/
```

## Common Commands

```bash
# View generated analysis
cat projects/MyProject/output/analysis/*.md

# View test cases
cat projects/MyProject/output/testcases/*.md

# Check logs
tail -f testcase_generation.log

# Run with fresh analysis (clear cache)
find projects -type d -name "cache" -exec rm -rf {} +
python generate_testcases.py

# Run specific project (edit generate_testcases.py line with PROJECT_FILTER)
PROJECT_FILTER=MyProject python generate_testcases.py
```

## Troubleshooting Quick Fixes

| Issue | Fix |
|-------|-----|
| "API key not found" | Check .env file exists and has valid keys |
| "ModuleNotFoundError" | Run: `pip install -r requirements.txt` |
| "No output files" | Verify BRD is in `projects/MyProject/input/BRD/` |
| "Analysis failed" | Check logs: `tail testcase_generation.log` |
| "Rate limit error" | Script auto-retries. Wait a few minutes |

## What Gets Generated

### Analysis Output
- Functional requirements breakdown
- UI components catalog
- Validation rules for each field
- Edge cases and boundaries
- Integration points
- Security requirements

### Test Cases
- Positive (happy path) scenarios
- Negative test cases
- Edge cases
- Field validation tests
- UI/UX tests
- Integration tests
- Security tests
- 50-100+ test cases per module

## Next Steps

1. Review generated files
2. Customize analysis by editing prompts
3. Export to your test management tool
4. Set up GitHub Actions for automation
5. Configure output formats (Excel, JSON, etc.)

## Getting Help

- Logs: `cat testcase_generation.log`
- Detailed guide: `README.md`
- Troubleshooting: `TROUBLESHOOTING.md`
- Configuration: `config.py`

---

**That's it! You're ready to generate test cases! 🚀**