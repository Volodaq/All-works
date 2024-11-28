import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        """
        Инициализация страницы формы с заданным драйвером.
        :param driver: Веб-драйвер (webdriver).
        """
        self.driver = driver
        self.waiter = WebDriverWait(driver, 40)

    @allure.step("Заполнение поля ")
    def fill_field(self, field_name: str, value: str) -> None:
        """
        Заполняет указанное текстовое поле значением.
        :param field_name: Имя поля (str).
        :param value: Значение для ввода (str).
        :return: None.
        """
        field = self.waiter.until(
            EC.presence_of_element_located((By.NAME, field_name))
        )
        field.send_keys(value)

    @allure.step("Отправка формы")
    def submit_form(self) -> None:
        """
        Отправляет заполненную форму.
        :return: None.
        """
        submit_button = self.waiter.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        submit_button.click()

    @allure.step("Получение цвета фона поля ")
    def get_field_background_color(self, field_id: str) -> str:
        """
        Получает цвет фона указанного поля.
        :param field_id: Идентификатор поля (str).
        :return: Цвет фона поля (str).
        """
        field = self.waiter.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return field.value_of_css_property('background-color')