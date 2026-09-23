from playwright.sync_api import expect

from pages.feedback_form_page import Feedback
from utils.email_generator_utility import GenerateEmailAndLogin
from utils.logger import get_logger
from utils.user_data_loader import get_feedback_forms_data

logger = get_logger("FeedbackFormsTests")


def test_feedback_form(page, base_url):
    feedback_form_page = Feedback(page)
    feedback_form_page.navigate_to_feedback_form(base_url)

    data = get_feedback_forms_data()

    logger.info("Verifying feedback form submission by a non-logged-in user")
    feedback_form_page.filling_feedback_forms(
        feedback_message=data["message"],
        company_name=data["company_name"],
        your_name=data["your_name"],
        your_email=GenerateEmailAndLogin.generate_email(),
        phone_number=data["phone_number"],
    )
    logger.info("Submitting the form by a non-logged-in user")

    expect(page.locator(feedback_form_page.FINAL_THANKYOU_PAGE)).to_be_visible()


def test_feedback_termination(page, base_url):
    feedback_form_page = Feedback(page)
    feedback_form_page.navigate_to_feedback_termination(base_url)

    data = get_feedback_forms_data()

    logger.info("Verifying feedback termination form submission by a non-logged-in user")
    feedback_form_page.filling_feedback_forms(
        feedback_message=data["message"],
        company_name=data["company_name"],
        your_name=data["your_name"],
        your_email=GenerateEmailAndLogin.generate_email(),
        phone_number=data["phone_number"],
    )
    logger.info("Submitting feedback termination form by a non-logged-in user")

    expect(page.locator(feedback_form_page.FINAL_THANKYOU_PAGE)).to_be_visible()


def test_feedback_support(page, base_url):
    feedback_form_page = Feedback(page)
    feedback_form_page.navigate_to_feedback_support(base_url)

    data = get_feedback_forms_data()

    logger.info("Verifying feedback support form submission by a non-logged-in user")
    feedback_form_page.filling_feedback_forms(
        feedback_message=data["message"],
        company_name=data["company_name"],
        your_name=data["your_name"],
        your_email=GenerateEmailAndLogin.generate_email(),
        phone_number=data["phone_number"],
    )
    logger.info("Submitting feedback support form by a non-logged-in user")

    expect(page.locator(feedback_form_page.FINAL_THANKYOU_PAGE)).to_be_visible()


def test_feedback_trade(page, base_url):
    feedback_form_page = Feedback(page)
    feedback_form_page.navigate_to_feedback_trade(base_url)

    data = get_feedback_forms_data()

    logger.info("Verifying feedback trade form submission by a non-logged-in user")
    feedback_form_page.filling_feedback_forms(
        feedback_message=data["message"],
        company_name=data["company_name"],
        your_name=data["your_name"],
        your_email=GenerateEmailAndLogin.generate_email(),
        phone_number=data["phone_number"],
        products_you_deal_in=data["products_you_deal_in"],
        buy_or_sell="Sell",
    )
    logger.info("Submitting feedback trade form by a non-logged-in user")

    expect(page.locator(feedback_form_page.FINAL_THANKYOU_PAGE)).to_be_visible()
