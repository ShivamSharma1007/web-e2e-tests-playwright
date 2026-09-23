from playwright.sync_api import expect

from pages.entity_view import EntityView
from utils.logger import get_logger
from utils.scroll_helper import ScrollHelper

logger = get_logger("EntityViewTest")


def test_buylead_view(page, base_url):
    page.goto(base_url)
    entity_view = EntityView(page)
    entity_view.navigating_to_buylead("rice")

    expect(page.locator(entity_view.BUYLEAD_TITLE).first).to_be_visible()
    buylead_title = page.locator(entity_view.BUYLEAD_VIEW_TITLE).inner_text().strip().lower()
    assert "rice" in buylead_title, (
        f"Rice buylead is not opened. Buylead title get: {buylead_title}"
    )


def test_product_view(page, base_url):
    page.goto(base_url)
    entity_view = EntityView(page)
    scroll_helper = ScrollHelper(page)

    # Navigating to the product view page - High Purity Copper Wire
    entity_view.navigating_to_product(base_url)

    logger.info("Checking if the product view title is visible")
    product_view_title = page.locator(entity_view.PRODUCT_VIEW_TITLE)
    expect(product_view_title).to_be_visible()

    product_title = product_view_title.inner_text().strip().lower()
    logger.info("Checking the text-High Purity Copper Wire in product title")
    assert "high purity copper wire" in product_title, (
        f"High Purity Copper Wire product is not opened. Product title get: {product_title}"
    )

    logger.info("Verifying the company name in the product view page")
    expect(page.locator(entity_view.COMPANY_NAME)).to_be_visible()

    logger.info("Verifying the view specifications button on product view page")
    view_specifications = page.locator(entity_view.VIEW_SPECIFICATIONS)
    expect(view_specifications).to_be_visible()

    logger.info("Clicking the view specifications button to check Full Specifications")
    view_specifications.click()
    logger.info("Verifying the specifications card is visible or not")
    expect(page.locator(entity_view.SPECIFICATIONS_CARD)).to_be_visible()

    scroll_helper.scroll_to_top()

    contact_supplier = page.locator(entity_view.CONTACT_SUPPLIER)
    expect(contact_supplier).to_be_visible()
    logger.info("Clicking the Contact Supplier button")
    contact_supplier.click()

    logger.info("Verifying the inquiry form is visible or not")
    expect(page.locator(entity_view.INQUIRY_FORM_HEADING)).to_be_visible()

    scroll_helper.scroll_to_top()

    logger.info("Verifying the key specifications card visible or not on the product view page")
    expect(page.locator(entity_view.KEY_SPECIFICATIONS_CARD)).to_be_visible()

    description_tab = page.locator(entity_view.DESCRIPTION_TAB)
    expect(description_tab).to_be_visible()
    logger.info("Clicking the Description tab")
    description_tab.click()
    logger.info("Verifying the Description card is visible or not")
    expect(page.locator(entity_view.DESCRIPTION_CARD)).to_be_visible()

    scroll_helper.scroll_to_top()

    # Specifications Tab
    specifications_tab = page.locator(entity_view.SPECIFICATIONS_TAB)
    expect(specifications_tab).to_be_visible()
    logger.info("Clicking the Specifications tab")
    specifications_tab.click()
    logger.info("Verifying the Specifications card is visible or not")
    expect(page.locator(entity_view.SPECIFICATIONS_CARD)).to_be_visible()

    scroll_helper.scroll_to_top()

    # Advantages Tab
    advantages_tab = page.locator(entity_view.ADVANTAGES_TAB)
    expect(advantages_tab).to_be_visible()
    logger.info("Clicking the Advantages tab")
    advantages_tab.click()
    logger.info("Verifying the Advantages card is visible or not")
    expect(page.locator(entity_view.ADVANTAGES_CARD)).to_be_visible()

    scroll_helper.scroll_to_top()

    # Other Details Tab
    other_details_tab = page.locator(entity_view.OTHER_DETAILS_TAB)
    expect(other_details_tab).to_be_visible()
    logger.info("Clicking the Other Details tab")
    other_details_tab.click()
    logger.info("Verifying the Other Details card is visible or not")
    expect(page.locator(entity_view.OTHER_DETAILS_CARD)).to_be_visible()

    scroll_helper.scroll_to_top()

    # Contact Tab - Inquiry Form Heading
    contact_tab = page.locator(entity_view.CONTACT_TAB)
    expect(contact_tab).to_be_visible()
    logger.info("Clicking the Contact tab")
    contact_tab.click()
    logger.info("Verifying the Inquiry Form Heading is visible or not")
    expect(page.locator(entity_view.INQUIRY_FORM_HEADING)).to_be_visible()

    scroll_helper.scroll_to_top()

    # FAQ Tab
    faq_tab = page.locator(entity_view.FAQ_TAB)
    expect(faq_tab).to_be_visible()
    logger.info("Clicking the FAQ tab")
    faq_tab.click()
    logger.info("Verifying the FAQ card is visible or not")
    expect(page.locator(entity_view.FAQ_CARD)).to_be_visible()

    scroll_helper.scroll_to_top()

    # Reviews Tab
    reviews_tab = page.locator(entity_view.REVIEWS_TAB)
    expect(reviews_tab).to_be_visible()
    logger.info("Clicking the Reviews tab")
    reviews_tab.click()
    logger.info("Verifying the Reviews card is visible or not")
    expect(page.locator(entity_view.REVIEWS_CARD)).to_be_visible()

    # Related Links
    expect(page.locator(entity_view.RELATED_CARD)).to_be_visible()
    logger.info("Verifying the Related Links section is visible")
    expect(page.locator(entity_view.RELATED_LINKS)).to_be_visible()


def test_member_view(page, context, base_url):
    page.goto(base_url)
    entity_view = EntityView(page)
    pages_before = len(context.pages)
    entity_view.navigating_to_member("shivam")

    try:
        if len(context.pages) == pages_before:
            new_page = context.wait_for_event("page", timeout=5000)
            new_page.wait_for_load_state()
            page = new_page
            entity_view = EntityView(page)
            logger.info(f"New windows length: {len(context.pages)}")
        elif len(context.pages) > pages_before:
            logger.info(f"New windows length: {len(context.pages)}")
            page = context.pages[-1]
            page.wait_for_load_state()
            entity_view = EntityView(page)
    except Exception:
        logger.info("New window not opened after clicking member's company name")

    expect(page.locator(entity_view.MEMBER_VIEW_TITLE)).to_be_visible()
    expect(page.locator(entity_view.MEMBER_ORIGIN)).to_be_visible()
    expect(page.locator(entity_view.SEND_INQUIRY_BUTTON)).to_be_visible()

    page.locator(entity_view.SEND_INQUIRY_BUTTON).click()
    expect(page.locator(entity_view.INQUIRY_FORM_HEADING)).to_be_visible()

    page.locator(entity_view.VIEW_PRODUCTS).click()
    expect(page.locator(entity_view.PRODUCT_SECTION)).to_be_visible()

    page.locator(entity_view.ABOUT_BUTTON).click()
    expect(page.locator(entity_view.ABOUT_SECTION)).to_be_visible()

    page.locator(entity_view.BUSINESS_PROFILE).click()
    expect(page.locator(entity_view.BUSINESS_SECTION)).to_be_visible()

    page.locator(entity_view.PRODUCTS_BUTTON).click()
    expect(page.locator(entity_view.PRODUCT_SECTION)).to_be_visible()

    page.locator(entity_view.ABOUT_BUTTON).click()
    expect(page.locator(entity_view.ABOUT_SECTION)).to_be_visible()

    page.locator(entity_view.CONTACT_BUTTON).click()
    expect(page.locator(entity_view.INQUIRY_FORM_HEADING)).to_be_visible()

    page.locator(entity_view.FAQ_BUTTON).click()
    expect(page.locator(entity_view.FAQ_CARD)).to_be_visible()

    page.locator(entity_view.REVIEWS_BUTTON).click()
    expect(page.locator(entity_view.REVIEWS_CARD)).to_be_visible()

    page.locator(entity_view.RELATED_BUTTON).click()
    expect(page.locator(entity_view.RELATED_LINKS)).to_be_visible()
