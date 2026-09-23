from playwright.sync_api import Page


class SearchPage:
    """
    Minimal Playwright SearchPage used by EntityView.
    Full SearchPage conversion when search_page.py is shared.
    """

    SEARCHBOX = "//input[@name= 'searchText']"
    SEARCH_BUYER = "//button[@id='FindBuyers']"
    SEARCH_SUPPLIERS = "//button[@id='FindSuppliers']"

    def __init__(self, page: Page):
        self.page = page

    def enter_search_text(self, text):
        self.page.locator(self.SEARCHBOX).fill(text)

    def click_search_buyer_button(self):
        self.page.locator(self.SEARCH_BUYER).click()

    def click_search_supplier_button(self):
        self.page.locator(self.SEARCH_SUPPLIERS).click()
