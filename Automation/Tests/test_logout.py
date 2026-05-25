from Automation.pages.login_page import LoginPage
from Automation.data.test_data import TestData


def test_logout(driver):

    driver.get(TestData.BASE_URL)

    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.login(
        TestData.VALID_EMAIL,
        TestData.VALID_PASSWORD
    )

    # Verify successful login first
    assert login_page.is_logged_in()

    login_page.click_logout()

    # Verify logout succeeded
    assert not login_page.is_logged_in()