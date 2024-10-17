from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()
    yield driver
    # Уберите эту строку, чтобы окно оставалось открытым
    # driver.quit()

def test_shopping_cart(driver):
    # 1. Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # 3. Нажать на кнопку Add to Cart для товаров
    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    for product in products:
        product_locator = (By.ID, f"add-to-cart-{product}")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(product_locator)
        ).click()

    # 4. Перейти в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажать Checkout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # 6. Заполнить форму своими данными
    driver.find_element(By.ID, "first-name").send_keys("Владимир")
    driver.find_element(By.ID, "last-name").send_keys("Валько")
    driver.find_element(By.ID, "postal-code").send_keys("250011")

    # 7. Нажать кнопку Continue
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # 8. Проверить, что итоговая сумма равна $58.29
    total_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    assert total_element.text == "Total: $58.29"

    # 9. Ожидание 15 секунд без использования time.sleep
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Finish')]"))
    )
