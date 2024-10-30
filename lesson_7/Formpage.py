from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_field(self, field_name, value):
        field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, field_name))
        )
        field.clear()
        field.send_keys(value)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        submit_button.click()

    def get_field_color(self, field_id):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return field.value_of_css_property('background-color')

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(driver):
    page = FormPage(driver)
    page.open()

    fields = {
        "first-name": "Владимир",
        "last-name": "Валько",
        "address": "Пушкина, 50",
        "e-mail": "test@skypro.com",
        "phone": "+79858999987",
        "zip-code": "",  # Ожидается красный цвет при пустом значении
        "city": "Бангкок",
        "country": "Таиланд",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for field_name, value in fields.items():
        page.fill_field(field_name, value)

    page.submit_form()

    # Проверка красного цвета для zip-code
    assert page.get_field_color("zip-code") == 'rgba(248, 215, 218, 1)'

    # Ожидаемый зелёный цвет для корректно заполненных полей
    expected_green_color = 'rgba(209, 231, 221, 1)'
    for field_id in ["first-name", "last-name", "address", "city", "e-mail", "phone", "job-position", "company"]:
        assert page.get_field_color(field_id) == expected_green_color
