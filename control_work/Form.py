import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields = {
        "first-name": "Владимир",
        "last-name": "Валько",
        "address": "Пушкина, 50",
        "e-mail": "test@skypro.com",
        "phone": "+79858999987",
        "zip-code": "",
        "city": "Бангкок",
        "country": "Таиланд",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for field_name, value in fields.items():
        field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, field_name)))
        field.send_keys(value)

    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
    submit_button.click()

    # Проверка цвета фона поля "Zip code" после отправки формы
    zip_code_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code")))
    zip_code_color = zip_code_element.value_of_css_property('background-color')
    expected_zip_code_color = 'rgba(248, 215, 218, 1)'
    assert zip_code_color == expected_zip_code_color, f"Expected Zip code background color: {expected_zip_code_color}, but got: {zip_code_color}"

    green_fields = ["first-name", "last-name", "address", "city", "e-mail", "phone", "job-position", "company"]
    expected_green_color = 'rgba(209, 231, 221, 1)'

    for field_id in green_fields:
        try:
            field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            field_color = field.value_of_css_property('background-color')
            assert field_color == expected_green_color, f"Expected background color for {field_id}: {expected_green_color}, but got: {field_color}"
        except Exception as e:
            print(f"Не удалось найти поле с ID {field_id} для проверки цвета фона. Ошибка: {e}")
