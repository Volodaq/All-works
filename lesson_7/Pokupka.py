import pytest
from selenium import webdriver
from Pokupkapage import ShoppingCartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping_cart(driver):
    page = ShoppingCartPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")

    for product_id in ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]:
        page.add_product_to_cart(product_id)

    page.go_to_cart()
    page.proceed_to_checkout()
    page.fill_checkout_form("Владимир", "Валько", "250011")

    assert page.get_total_price() == "Total: $58.29"
