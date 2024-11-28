import allure
import pytest
from selenium import webdriver
from ShopPage import ShopCartPage


@pytest.fixture(scope="function")
def driver() -> webdriver.Chrome:
    """Инициализация WebDriver для тестов.”
    Создает и настраивает экземпляр Chrome WebDriver.
        :return: Экземпляр WebDriver (Chrome).
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест корзины покупок")
@allure.description("Проверка функциональности корзины покупок на сайте.")
@allure.feature("Покупка товаров")
def test_shopping_cart(driver):
    """Тест процесса покупок на сайте."""
    with allure.step("Страница сайта"):
    driver.get("https://www.saucedemo.com/")
    shop_cart_page = ShopCartPage(driver)

    with allure.step("Вход в систему"):
    shop_cart_page.login("standard_user", "secret_sauce")

    with allure.step("Список продуктов для добавления в корзину"):
    products = ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt",
                "sauce-labs-onesie"]

    with allure.step("Добавление продуктов в корзину"):
    shop_cart_page.add_products_to_cart(products)
    shop_cart_page.go_to_cart()

    with allure.step("Оформление заказа"):
    shop_cart_page.checkout("Vladimir", "Valko", "776655")

    with allure.step("Получение общей суммы и проверка её правильности"):
    total_text = shop_cart_page.get_total()
    assert total_text == "Total: $58.29", (
        f"Ожидалась сумма: Total: $58.29, но получено: {total_text}"
    )

    with allure.step("Завершение покупки"):
    shop_cart_page.complete_purchase()