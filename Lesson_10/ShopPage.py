import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopCartPage:
    def __init__(self, driver):
        """
        Инициализация страницы корзины с экземпляром WebDriver.
        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self.driver = driver
        self.waiter = WebDriverWait(driver, 40)

    @allure.step("Вход с использованием учетных данных пользователя")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход на сайт покупок с использованием предоставленных
          учетных данных.
        :param username: Имя пользователя для входа.
        :param password: Пароль для входа.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @allure.step("Добавление продуктов в корзину")
    def add_products_to_cart(self, products: list) -> None:
        """
        Добавляет список продуктов в корзину.
        :param products: Список идентификаторов продуктов, которые нужно
        добавить в корзину.
        """
        for product in products:
            product_locator = (By.ID, f"add-to-cart-{product}")
            self.waiter.until(EC.element_to_be_clickable(product_locator)
                              ).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины покупок.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step("Оформление заказа с информацией пользователя")
    def checkout(self, first_name: str, last_name: str,
                 postal_code: str) -> None:
        """
        Завершает процесс оформления заказа с информацией пользователя.
        :param first_name: Имя пользователя.
        :param last_name: Фамилия пользователя.
        :param postal_code: Почтовый код для адреса.
        """
        self.waiter.until(EC.element_to_be_clickable((By.ID, "checkout"))
                          ).click()
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @allure.step("Получение общей суммы из корзины")
    def get_total(self) -> str:
        """
        Получает общую сумму, отображаемую в корзине.
        :return: Общая сумма в виде строки.
        """
        return self.waiter.until(
            EC.visibility_of_element_located((By.CLASS_NAME,
                                              "summary_total_label"))
        ).text

    @allure.step("Завершение покупки")
    def complete_purchase(self) -> None:
        """
        Завершает процесс покупки.
        """
        self.waiter.until(EC.element_to_be_clickable((By.ID, "finish"))
                          ).click()