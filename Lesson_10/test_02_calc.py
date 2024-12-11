import pytest
import allure
from selenium import webdriver
from CalcPage import CalculatorPage  # Импортируем класс


@pytest.fixture
def driver() -> webdriver.Chrome:
    """
    Инициализация WebDriver (например, Chrome).

    :return: Экземпляр WebDriver (Chrome).
    """
    driver = webdriver.Chrome()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver
    driver.quit()


@allure.title("Тест на сложение")
@allure.description("Проверка функции сложения в медленном калькуляторе")
@allure.feature("Сложение")
@allure.severity(allure.severity_level.NORMAL)
def test_addition(driver):
    calculator = CalculatorPage(driver)

    with allure.step("Установка задержки в 45 секунд"):
         calculator.set_delay("45")

    with allure.step("Выполнение сложения 7 + 8"):
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')

    with allure.step("Ожидание, пока результат не будет отображен"):
        calculator.wait_for_result("15")

    with allure.step("Получение результата и проверка"):
        result = calculator.get_result()
        assert result == '15', "Ожидалось, что результат будет '15', но получено '{result}'"