from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    input_field.send_keys("1000")

    time.sleep(4)

    input_field.clear()

    time.sleep(3)

    input_field.send_keys("999")

    time.sleep(5)

finally:
    driver.quit()
