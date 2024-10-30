import pytest
from selenium import webdriver
from Formpage import FormPage

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
        "zip-code": "",
        "city": "Бангкок",
        "country": "Таиланд",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for field_name, value in fields.items():
        page.fill_field(field_name, value)

    page.submit_form()

    assert page.get_field_color("zip-code") == 'rgba(248, 215, 218, 1)'
    expected_green_color = 'rgba(209, 231, 221, 1)'

    for field_id in ["first-name", "last-name", "address", "city", "e-mail", "phone", "job-position", "company"]:
        assert page.get_field_color(field_id) == expected_green_color
