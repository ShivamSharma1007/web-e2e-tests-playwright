import json
import os

from dotenv import load_dotenv

load_dotenv()


def load_json_data(data_path):
    """
    Loads a JSON file and returns its data as a dictionary.
    """
    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_invalid_user_data(data_path="testdata/user_data.json"):
    """
    Loads user data from JSON file.
    """
    return load_json_data(data_path)


def get_user_signup_data(data_path="testdata/signup_test_data.json"):
    """
    Returns user signup test data.
    """
    return load_json_data(data_path)


def get_user_buylead_data(data_path="testdata/buylead_form_data.json"):
    """
    Returns positive buylead form test data.
    """
    return load_json_data(data_path)["positive_test_data"]


def get_product_upload_data(data_path="testdata/product_upload_data.json"):
    """
    Returns product upload form test data.
    """
    return load_json_data(data_path)["product_upload_data"]


def get_feedback_forms_data(data_path="testdata/feedback_forms_data.json"):
    """
    Returns feedback form test data.
    """
    return load_json_data(data_path)["feedback_forms_data"]


def get_inquiry_data(data_path="testdata/inquiry_data.json"):
    """
    Returns inquiry test data.
    """
    return load_json_data(data_path)


def get_valid_user():
    """
    Returns valid user credentials from environment variables.
    """
    return {
        "email": os.environ.get("TEST_VALID_USER_EMAIL"),
        "password": os.environ.get("TEST_VALID_USER_PASSWORD")
    }


def get_valid_gold_user():
    """
    Returns valid Gold user credentials from environment variables.
    """
    return {
        "email": os.environ.get("TEST_GOLD_USER_EMAIL"),
        "password": os.environ.get("TEST_GOLD_USER_PASSWORD")
    }


def get_valid_user_for_decline_inquiry():
    """
    Returns valid user credentials for decline inquiry scenarios.
    """
    return {
        "email": os.environ.get("TEST_DECLINE_INQUIRY_USER_EMAIL"),
        "password": os.environ.get("TEST_DECLINE_INQUIRY_USER_PASSWORD")
    }


def get_valid_user_for_decline_buylead_inquiry():
    """
    Returns valid user credentials for decline buylead inquiry scenarios.
    """
    return {
        "email": os.environ.get("TEST_DECLINE_BUYLEAD_INQUIRY_USER_EMAIL"),
        "password": os.environ.get("TEST_DECLINE_BUYLEAD_INQUIRY_USER_PASSWORD")
    }


def get_auth_code():
    """
    Returns authentication code from environment variables.
    """
    return {
        "auth_code": os.environ.get("AUTH_CODE")
    }


def get_valid_coupon_for_all_plans():
    """
    Returns valid coupons for all membership plans.
    """
    return {
        "valid_coupon": os.environ.get("VALID_COUPON"),
        "goldplus_plan": os.environ.get("VALID_COUPON_FOR_GP"),
        "gold_plan": os.environ.get("VALID_COUPON_FOR_GL"),
        "silver_plan": os.environ.get("VALID_COUPON_FOR_SL"),
        "go4mywebsite_plan": os.environ.get("VALID_COUPON_FOR_WB")
    }

