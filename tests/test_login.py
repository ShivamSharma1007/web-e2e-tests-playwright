from pages.loginpage import LoginPage
from utils.user_data_loader import get_valid_user, load_invalid_user_data,get_valid_gold_user,get_auth_code
from utils.logger import get_logger
from playwright.sync_api import expect

logger = get_logger("TestLogin.py")

def test_valid_login(page, base_url):
    login_page = LoginPage(page)
    page.goto(base_url+"/login")
    user =get_valid_user()

    login_page.login(user["email"], user["password"])
    expect(login_page.PROFILE_DROPDOWN).to_contain_text(user["email"])
    assert f"{user["email"]}" in page.content()

def test_invalid_login(page,base_url):
    login_page = LoginPage(page)
    page.goto(base_url+"/login")
    invalid_user = load_invalid_user_data()
    user = invalid_user["invalid_user"]

    login_page.login(user["email"],user["password"])
    assert "Invalid credentials" in page.content()

def test_gold_user_with_auth(page,base_url):
    login_page =LoginPage(page)
    page.goto(base_url+"/login")
    user = get_valid_gold_user()
    bypass_otp = get_auth_code()

    login_page.login(user["email"],user["password"])
    try:
        if login_page.AUTHENTICATION_PAGE.is_displayed():
            login_page.submit_auth_code(bypass_otp)
    except:
        page.goto("https://api.ipify.org/?format=text")
        current_ip = page.locator("body").inner_text()
        assert "180.151.31.14" in current_ip, f"Authentication is bypassed on IP: {current_ip}"
        logger.info(f"Authentication code bypassed on IP: {current_ip}")