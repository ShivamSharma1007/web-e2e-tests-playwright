from playwright.sync_api import Page, expect

from pages.search_page import SearchPage
from utils.user_data_loader import get_inquiry_data


class EntityView:

    BUYLEAD_TITLE = "//h2[@class='text-capitalize entity-row-title h2-item-title']/span"
    PRODUCT_TITLE = "//h2[@class= 'text-capitalize entity-row-title h2-item-title ellipsis product-title']"
    MEMBER_TITLE = "//a[@href='/member/view/3788618/shivam-masks.html']"
    PRODUCT_VIEW_TITLE = "//h1[contains(text(),'High Purity Copper Wire')]"
    BUYLEAD_VIEW_TITLE = "//h1[@align='center']"
    MEMBER_VIEW_TITLE = "//h1[@class='nev-entity-title']"

    # Locators for product view page
    COMPANY_NAME = "//div[@class='pn-v3-supplier-name']"
    VIEW_SPECIFICATIONS = "//div[@class='pn-v3-actions']//a[@class='pn-btn pn-v3-btn pn-v3-btn-secondary']"
    CONTACT_SUPPLIER = "//a[@class='pn-btn pn-v3-btn pn-v3-supplier-contact']"
    VIEW_ALL_PRODUCT = "//div[@class='pn-v3-supplier-actions']//a[@class='pn-btn pn-v3-btn pn-v3-btn-secondary']"
    KEY_SPECIFICATIONS_CARD = "//h3[contains(text(),'Key Specifications')]"

    PRODUCT_SECTIONS = "//nav[@aria-label='Product sections']"
    DESCRIPTION_TAB = "//a[@href='#description']"
    DESCRIPTION_CARD = "//h3[contains(text(),'Product Description')]"
    SPECIFICATIONS_TAB = "//nav[@aria-label='Product sections']//a[@href='#specs']"
    SPECIFICATIONS_CARD = "//h3[contains(text(),'Full Specifications')]"
    ADVANTAGES_TAB = "//a[@href='#advantages']"
    ADVANTAGES_CARD = "//h3[contains(text(),'Competitive Advantages')]"
    OTHER_DETAILS_TAB = "//a[@href='#other-details']"
    OTHER_DETAILS_CARD = "//h3[contains(text(),'Other Details')]"
    CONTACT_TAB = "//nav[@aria-label='Product sections']//a[@href='#contact']"
    INQUIRY_FORM_HEADING = "//div[contains(text(),'Send Inquiry')]"
    FAQ_TAB = "//a[@href='#faq']"
    FAQ_CARD = "//h3[contains(text(),'Frequently Asked Questions')]"
    REVIEWS_TAB = "//a[@href='#reviews']"
    REVIEWS_CARD = "//h3[contains(text(),'Recent User Reviews')]"
    RELATED_CARD = "//h3[contains(text(),'Related')]"
    RELATED_LINKS = "//div[@class='nev-related-links mar-top-10']"

    # Locators for member view page
    MEMBER_ORIGIN = "//div[@class='nev-entity-origin']"
    SEND_INQUIRY_BUTTON = "//div[@class='pn-v3-actions']//a[@href='#contact']"
    VIEW_PRODUCTS = "//a[contains(text(),'View Products')]"
    ABOUT = "//div[@class='pn-v3-actions']//a[contains(text(),'About')]"

    PRODUCT_SECTION = "//h2[@class='mn-products-showcase-title nev-section-heading']"
    ABOUT_SECTION = "//h2[contains(text(),'About')]"
    BUSINESS_PROFILE = "//a[contains(text(),'Business Profile')]"
    BUSINESS_SECTION = "//h2[contains(text(),'Business Profile')]"
    ABOUT_BUTTON = "//nav[@class='mn-nav']//a[contains(text(),'About')]"
    PRODUCTS_BUTTON = "//nav[@class='mn-nav']//a[contains(text(),'Products')]"
    CONTACT_BUTTON = "//nav[@class='mn-nav']//a[contains(text(),'Contact')]"
    FAQ_BUTTON = "//nav[@class='mn-nav']//a[contains(text(),'FAQ')]"
    REVIEWS_BUTTON = "//nav[@class='mn-nav']//a[contains(text(),'Reviews')]"
    RELATED_BUTTON = "//nav[@class='mn-nav']//a[contains(text(),'Related')]"

    def __init__(self, page: Page):
        self.page = page
        self.search_page = SearchPage(self.page)

    def navigating_to_buylead(self, text):
        self.search_page.enter_search_text(text)
        self.search_page.click_search_buyer_button()
        buylead_titles = self.page.locator(self.BUYLEAD_TITLE)
        expect(buylead_titles.first).to_be_visible()
        buylead_titles.first.click()

    def navigating_to_product(self, base_url):
        testdata = get_inquiry_data()
        self.page.goto(
            base_url + testdata["URL"]["product_url"]
        )

    def navigating_to_member(self, text):
        self.search_page.enter_search_text(text)
        self.search_page.click_search_supplier_button()
        member_titles = self.page.locator(self.MEMBER_TITLE)
        expect(member_titles.first).to_be_visible()
        member_titles.first.click()
