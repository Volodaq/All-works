
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver,40)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def add_product_to_cart(self, product_id):
        product_locator = (By.ID, f"add-to-cart-{product_id}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(product_locator)
        ).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def get_total_price(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
