import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора с заданным драйвером.

        :param driver: Веб-драйвер (webdriver).
        """
        self.driver = driver
        self.waiter = WebDriverWait(driver, 46)

    @allure.step("Установка задержки")
    def set_delay(self, delay: str) -> None:
        """
        Устанавливает задержку в поле ввода.

        :param delay: Задержка для установки.
        :return: None.
        """
        delay_field = self.waiter.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#delay")))
        delay_field.clear()
        delay_field.send_keys(delay)

    @allure.step("Нажатие кнопки '{button}'")
    def click_button(self, button: str) -> None:
        """
        Нажимает на заданную кнопку.

        :param button: Текст кнопки, на которую нужно нажать (str).
        :return: None.
        """
        button_element = self.waiter.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']")
                                       ))
        button_element.click()

    @allure.step("Получение результата")
    def get_result(self) -> str:
        """
        Получает текст результата с экрана.

        :return: Результат (str).
        """
        result_locator = (By.CSS_SELECTOR, ".screen")
        return self.waiter.until(EC.presence_of_element_located(result_locator)
                                 ).text

    @allure.step("Ожидание результата '{expected_result}'")
    def wait_for_result(self, expected_result: str) -> None:
        """
        Ожидает появления ожидаемого результата на экране.

        :param expected_result: Ожидаемый результат (str).
        :return: None.
        """
        self.waiter.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '.screen'), str(expected_result)))