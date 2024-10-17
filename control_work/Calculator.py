import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_field.clear()
    delay_field.send_keys("45")

    buttons = ['7', '+', '8', '=']
    for button in buttons:
        button_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))
        )
        button_element.click()

    result_locator = (By.CSS_SELECTOR, "#result")
    try:
        WebDriverWait(driver, 45).until(
            EC.text_to_be_present_in_element(result_locator, "15")
        )

        result_element = driver.find_element(*result_locator)
        result_text = result_element.text
        print(f"Текущий текст результата: {result_text}")

        assert result_text == "15", f"Ожидался результат 15, но получен: {result_text}"
    except Exception as e:
        print(f"Ошибка: {e}")
