from Automation.pages.login_page import LoginPage
from Automation.data.test_data import TestData

def test_search_product(driver):
    driver.get(TestData.BASE_URL)

    page = LoginPage(driver)

    page.search_product(TestData.SEARCH_PRODUCT)

    assert page.is_search_results_displayed()