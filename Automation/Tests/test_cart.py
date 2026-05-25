from Automation.pages.login_page import LoginPage
from Automation.data.test_data import TestData

def test_add_product_to_cart(driver):
    driver.get(TestData.BASE_URL)

    page = LoginPage(driver)

    page.search_product(TestData.SEARCH_PRODUCT)

    page.add_first_product_to_cart()

    page.open_cart()

    assert page.is_item_in_cart()