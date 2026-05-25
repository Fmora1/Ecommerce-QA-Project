import pytest
from Automation.pages.login_page import LoginPage
from Automation.data.test_data import TestData

@pytest.mark.parametrize(
    "email,password",
    [
        ("wrong_user@example.com", "WrongPassword123"),
        ("invalid@gmail.com", "badpass"),
    ],
    ids=[
        "invalid_email_and_password",
        "random_invalid_credentials",
    ]
)


def test_invalid_login(driver, email, password):

    driver.get(TestData.BASE_URL)

    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.login(email, password)

    assert login_page.invalid_login_error_displayed()