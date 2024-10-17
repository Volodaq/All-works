import pytest
import time  # Добавляем импорт модуля time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(driver):
    # Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнить форму с явными ожиданиями для каждого элемента
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",  # оставить пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for field_name, value in fields.items():
        field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, field_name))
        )
        field.send_keys(value)

    # Нажать кнопку Submit
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
    )
    submit_button.click()

    # Проверяем, что окно остается открытым 15 секунд
    start_time = time.monotonic()
    while True:
        if time.monotonic() - start_time > 15:
            break
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))  # Проверяем, что страница не закрыта
