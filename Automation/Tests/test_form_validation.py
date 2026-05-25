from Automation.pages.login_page import LoginPage
from Automation.data.test_data import TestData


def test_email_field_is_required(driver):

    driver.get(TestData.BASE_URL)

    page = LoginPage(driver)

    page.open_login_page()

    assert page.is_email_field_required()


def test_password_field_is_required(driver):

    driver.get(TestData.BASE_URL)

    page = LoginPage(driver)

    page.open_login_page()

    assert page.is_password_field_required()