from playwright.sync_api import Page


class Feedback:

    # Locators for common feedback forms
    FEEDBACK_MESSAGE = "//textarea[@id = 'feedback_message']"
    COMPANY_NAME = "//input[@id = 'feedback_companyName']"
    YOUR_NAME = "//input[@id = 'feedback_name']"
    YOUR_EMAIL = "//input[@id = 'feedback_email']"
    PHONE_NUMBER = "//input[@id = 'feedback_phone']"
    SUBMIT_BUTTON = "//div[@class='form-group']//button[@type='submit']"
    FINAL_THANKYOU_PAGE = "//h1[@class = 'text-center']"

    # Locators for feedback trade form
    BUY_OR_SELL_BUTTON = "//input[@id = 'feedback_buyOrSell_1']"
    PRODUCT_YOU_DEAL_IN = "//input[@id='feedback_product']"

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_feedback_form(self, base_url):
        self.page.goto(base_url + "/feedback")

    def navigate_to_feedback_termination(self, base_url):
        self.page.goto(base_url + "/feedback/termination")

    def navigate_to_feedback_ceo(self, base_url):
        self.page.goto(base_url + "/feedback/ceo")

    def navigate_to_feedback_manager(self, base_url):
        self.page.goto(base_url + "/feedback/manager")

    def navigate_to_feedback_support(self, base_url):
        self.page.goto(base_url + "/feedback/support")

    def navigate_to_feedback_trade(self, base_url):
        self.page.goto(base_url + "/feedback/trade")

    def filling_feedback_forms(
        self,
        feedback_message,
        company_name,
        your_name,
        your_email,
        phone_number,
        buy_or_sell=None,
        products_you_deal_in=None,
    ):
        if buy_or_sell:
            self.page.locator(self.BUY_OR_SELL_BUTTON).click()

        if products_you_deal_in:
            self.page.locator(self.PRODUCT_YOU_DEAL_IN).fill(products_you_deal_in)

        self.page.locator(self.FEEDBACK_MESSAGE).fill(feedback_message)
        self.page.locator(self.COMPANY_NAME).fill(company_name)
        self.page.locator(self.YOUR_NAME).fill(your_name)
        self.page.locator(self.YOUR_EMAIL).fill(your_email)
        self.page.locator(self.PHONE_NUMBER).fill(phone_number)

        submit_buttons = self.page.locator(self.SUBMIT_BUTTON)
        assert submit_buttons.count() == 1, (
            f"Expected 1 submit button but found {submit_buttons.count()}"
        )
        submit_buttons.first.click()
