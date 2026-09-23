<<<<<<< HEAD
# playwright-tests

End-to-end automation framework for go4WorldBusiness using Playwright and Pytest, covering critical user flows, UI validation, and regression testing.

## 🚀 Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd playwright-tests
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt

# Run tests
py -m pytest
```

## 📁 Project Structure

```
playwright-tests/ 
│ 
├── pages/ # Page Object Model classes   
├── tests/ # Test cases 
├── utils/ # Utility modules
├── config/ # Environment and Playwright configuration 
├── testdata/ # Test data files
├── reports/ # Test reports and screenshots 
├── conftest.py # Global Pytest fixtures 
```

## 🧪 Running Tests

### Basic Commands
```bash
Run All Tests
py -m pytest
##Run a Specific Test File
py -m pytest tests/test_login.py
##Run a Specific Test
py -m pytest tests/test_login.py::test_valid_login
##Run Tests in Parallel
##If pytest-xdist is installed:
py -m pytest -n 4
```

### Environment & Options
```bash
pytest --env=staging             # Run on staging environment
pytest --env=prod               # Run on production environment
pytest --send-report-email      # Send email report after tests
pytest --env=prod --send-report-email  # Combine options
```

### Reports
- **HTML Report**: Automatically generated in `reports/report.html`
- **Email Report**: Optional, sent when `--send-report-email` is used

## 📧 Email Reports

### Setup
1. Copy the environment template: `cp env_template.txt .env`
2. Configure SendGrid settings in `.env`:
   - `SENDGRID_API_KEY`: Your SendGrid API key
   - `TO_EMAIL_ADDRESS`: Recipient email
   - `FROM_EMAIL_ADDRESS`: Verified sender email
   - `EMAIL_SUBJECT`: Custom subject (optional)

### Usage
```bash
pytest --send-report-email  # Send email after tests
python send_report_email.py  # Send report manually
```

### Email Content
- Test execution summary (total, passed, failed, skipped)
- Success rate percentage
- Individual test results with pass/fail status
- Timestamp and project information

## 🚀 CI/CD Setup

### Driver Configuration
- **Centralized**: All Chrome options in `config/config.yaml`
- **CI/CD Optimized**: Includes flags for containerized environments
- **Global Fixture**: `driver` fixture available in all test files

### Configuration
```yaml
chrome_options:
  essential_flags:
    - "--no-sandbox"
    - "--disable-dev-shm-usage"
    - "--disable-gpu"
  stability_flags:
    - "--disable-extensions"
    - "--disable-plugins"
    - "--disable-images"
    - "--disable-web-security"
    - "--allow-running-insecure-content"
  window_size: "--window-size=1920,1080"
  headless_flag: "--headless=new"
```

### Using Driver Fixture
```python
def test_example(driver, base_url):
    driver.get(base_url)
    # Your test code here
```

### Environment Variables
```bash
# Email functionality
SENDGRID_API_KEY=your_sendgrid_api_key
TO_EMAIL_ADDRESS=recipient@example.com
FROM_EMAIL_ADDRESS=your_verified_sender@example.com

# Test credentials
VALID_USER_EMAIL=test@example.com
VALID_USER_PASSWORD=test_password
```

### Common Issues Fixed
- ✅ `SessionNotCreatedException` - Fixed with unique user data directory
- ✅ Memory issues - Fixed with `--disable-dev-shm-usage` and `--no-sandbox`
- ✅ Permission issues - Fixed with proper Chrome flags
- ✅ Environment variables - Fixed with early `load_dotenv()` call

## 📝 Development

### Adding New Tests
- Place test files in the `tests/` directory
- Use the `driver` fixture (automatically available)
- Use utilities in `utils/` for config, logging, and data

### Configuration
- **Environments**: Update `config/config.yaml`
- **Test Data**: Update `testdata/user_data.json`
- **Chrome Options**: Modify `chrome_options` in config 
=======
# web-e2e-tests-playwright
End-to-end automation framework for go4WorldBusiness using Playwright and Pytest, covering critical user flows, UI validation, and regression testing.
>>>>>>> 7fc2074e46ad3227834a1ffe708642e7db8bf283
