from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # --- Authentication Locators ---
        self.login_link = (By.LINK_TEXT, "Signup / Login")
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[text()='Login']")
        self.logged_in_text = (By.XPATH, "//*[contains(text(),'Logged in as')]")
        self.invalid_login_message = (By.XPATH, "//*[contains(text(),'incorrect')]")
        self.logout_link = (By.LINK_TEXT, "Logout")

        # --- Search & Cart Locators ---
        self.products_link = (By.PARTIAL_LINK_TEXT, "Products")
        self.search_input = (By.ID, "search_product")
        self.search_button = (By.ID, "submit_search")
        self.search_results_title = (By.XPATH, "//h2[text()='Searched Products']")
        self.add_to_cart_btn = (By.XPATH, "(//a[text()='Add to cart'])[1]")
        self.continue_shopping_btn = (By.XPATH, "//button[text()='Continue Shopping']")
        self.cart_link = (By.PARTIAL_LINK_TEXT, "Cart")
        self.cart_item = (By.CLASS_NAME, "cart_description")

    # --- Original Login Methods ---
    def open_login_page(self):
        self.wait.until(EC.element_to_be_clickable(self.login_link)).click()

    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        try:
            # If the element is found within 10 seconds, return True
            self.wait.until(EC.presence_of_element_located(self.logged_in_text))
            return True
        except TimeoutException:
            # If it times out (like after clicking logout), return False safely
            return False

    def invalid_login_error_displayed(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(self.invalid_login_message)
            )
            return True
        except TimeoutException:
            return False

    # --- New Upgrade: Logout Method ---
    def click_logout(self):

        logout_element = self.wait.until(
            EC.presence_of_element_located(self.logout_link)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout_element
        )

    # --- New Upgrade: Search Methods ---
    def search_product(self, product_name):
        # 1. Wait until the 'Products' link is completely clickable and click it
        products_btn = self.wait.until(EC.element_to_be_clickable(self.products_link))

        # Safe click bypass for ad overlays
        self.driver.execute_script("arguments[0].click();", products_btn)

        # 2. Wait until the search field is visible and ready on the new page
        search_field = self.wait.until(EC.visibility_of_element_located(self.search_input))

        # 3. Clear any default text and type the product name
        search_field.clear()
        search_field.send_keys(product_name)

        # 4. Click the search button
        self.driver.find_element(*self.search_button).click()

    def is_search_results_displayed(self):
        return bool(self.wait.until(EC.presence_of_element_located(self.search_results_title)))

    # --- New Upgrade: Add-to-Cart Methods ---

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_link)).click()

    def is_item_in_cart(self):
        return bool(self.wait.until(EC.presence_of_element_located(self.cart_item)))

    # Add this method inside your LoginPage class in login_page.py
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def add_first_product_to_cart(self):
        # Wait for the button to be present on the DOM layout
        element = self.wait.until(EC.presence_of_element_located(self.add_to_cart_btn))

        # Use JavaScript to click directly, bypassing any ad overlay blocks
        self.driver.execute_script("arguments[0].click();", element)

        # Safely click continue using standard wait
        self.wait.until(EC.element_to_be_clickable(self.continue_shopping_btn)).click()

    def is_email_field_required(self):
        field = self.driver.find_element(*self.email_input)
        return field.get_attribute("required") is not None

    def is_password_field_required(self):
        field = self.driver.find_element(*self.password_input)
        return field.get_attribute("required") is not None
