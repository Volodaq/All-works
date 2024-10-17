from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
    button.click()

    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content")))

    print(message.text)

    input("Enter")

finally:
    driver.quit()
