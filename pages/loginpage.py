class LoginPage:
    def __init__(self,page):
        self.page=page

    # Locators
        self.SIGN_IN_WITH_PASSWORD = page.locator("#login-otp-toggle")
        self.EMAIL = page.get_by_placeholder("Username")
        self.PASSWORD = page.get_by_placeholder("Password")
        self.LOGIN = page.locator("//button[@class='btn btn-default site-btn login-btn']")
        self.PROFILE_DROPDOWN = page.locator("//li[@class='dropdown pull-left hidden-xs']")
        self.AUTHENTICATION_PAGE = page.locator("//form[@class='form']")
        self.AUTH_CODE_FIELD = page.locator("//input[@id='_auth_code']")
        self.AUTH_CODE_SUBMIT_BUTTON = page.locator("//button[@name='_authenticate']")

    def login(self,email,password):
        self.SIGN_IN_WITH_PASSWORD.click()
        self.EMAIL.fill(email)
        self.PASSWORD.fill(password)
        self.LOGIN.click()

    def submit_auth_code(self,bypass_otp):
        self.AUTH_CODE_FIELD.fill(bypass_otp)
        self.AUTH_CODE_SUBMIT_BUTTON.click()