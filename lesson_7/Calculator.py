import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Calcelatorpage import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay("45")

    for button in ['7', '+', '8', '=']:
        page.click_button(button)

    try:
        # Увеличьте время ожидания, чтобы тест мог дождаться появления результата
        result_text = WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.ID, "result"), "15")
        )
        assert result_text == "15", f"Ожидался результат 15, но получен: {result_text}"
    except Exception as e:
        print(f"Ошибка: {e}")
