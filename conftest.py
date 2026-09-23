import pytest
import os

from playwright.sync_api import sync_playwright
from utils.screenshot_util import ScreenshotUtil
from utils.config_loader import load_config

# Load configuration

def pytest_addoption(parser):
    parser.addoption(
    "--send-report-email",
    action="store_true",
    default=False,
    help="Send email report after test execution"
    )

@pytest.fixture(scope="session")
def config():
    """
    Load complete configuration from config/config.yaml.
    Environment is selected from the 'env' value in config.yaml.
    """
    return load_config()

@pytest.fixture(scope="session")
def base_url(config):
    """
    Return base URL for the environment configured in config.yaml.
    Example:
    env: staging
    -> https://uat2.go4worldbusiness.com
    """

    env = config["env"] 
    base_urls = config["base_urls"]

    if env not in base_urls:
        raise ValueError(
            f"Environment '{env}' is not configured in config.yaml. "
            f"Available environments: {list(base_urls.keys())}"
        )

    return base_urls[env]

# Playwright
@pytest.fixture(scope="session")
def playwright():
    """
    Start Playwright once for the complete test session.
    """
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright, config):
    """
    Create browser based on config.yaml.
    """

    browser_name = config.get("browser", "chromium")
    headless = config.get("headless", False)

    browser_options = config.get("browser_options", {})
    args = browser_options.get("args", [])

    if browser_name == "chromium":
        browser = playwright.chromium.launch(
            headless=headless,
            args=args
        )

    elif browser_name == "firefox":
        browser = playwright.firefox.launch(
            headless=headless
        )

    elif browser_name == "webkit":
        browser = playwright.webkit.launch(
            headless=headless
        )

    else:
        raise ValueError(
            f"Unsupported browser '{browser_name}'. "
            f"Supported browsers: chromium, firefox, webkit"
        )

    yield browser

    browser.close()

@pytest.fixture(scope="function")
def context(browser, config):
    """
    Create a new browser context for every test.
    """

    browser_options = config.get("browser_options", {})
    viewport = browser_options.get("viewport", {})

    context = browser.new_context(
        viewport={
            "width": viewport.get("width", 1920),
            "height": viewport.get("height", 1080)
        }
    )

    yield context

    context.close()

@pytest.fixture(scope="function")
def page(context, config):
    """
    Create a new Playwright page for every test.
    """

    page = context.new_page()

    timeouts = config.get("timeouts", {})

    page.set_default_timeout(
        timeouts.get("default", 30000)
    )

    page.set_default_navigation_timeout(
        timeouts.get("navigation", 30000)
    )

    yield page

    page.close()

# Screenshots
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    page = item.funcargs.get("driver", None)
    if page and rep.when == "call":
        # Always take a screenshot after each test
        ScreenshotUtil.save_screenshot(page, name_prefix=f"{item.name}_{rep.outcome}")
        
# Email Report