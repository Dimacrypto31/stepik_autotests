import math

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.XPATH, '//*[contains(@id, "num1")]')
    num2 = browser.find_element(By.XPATH, '//*[contains(@id, "num2")]')
    n1 = num1.text
    n2 = num2.text
    nm3 = int(n1) + int(n2)
    nm = str(nm3)

    browser.find_element(By.XPATH, '//*[contains(@class, "custom-select")]').click()
    browser.find_element(By.CSS_SELECTOR, (f"[value='{nm}']")).click()


    button = browser.find_element(By.XPATH, "//*[contains(@class, 'btn btn-default')]")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
