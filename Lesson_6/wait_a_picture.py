from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 15)
    images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))

    print(f"Найдено изображений: {len(images)}")

    if len(images) >= 3:
        third_image = images[2]  # Индекс 2 = третья картинка

        src_value = third_image.get_attribute("src")

        print(f"Значение src третьей картинки: {src_value}")
    else:
        print()

    input()

finally:
    driver.quit()
