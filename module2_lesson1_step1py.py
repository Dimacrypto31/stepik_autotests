import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//*[contains(@class, "btn btn-primary")]').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    xelem = browser.find_element(By.XPATH, '//*[contains(@id, "input_value")]')
    x = xelem.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, '//*[contains(@class, "form-control")]')
    input1.send_keys(y)


    button = browser.find_element(By.XPATH, '//*[contains(@type, "submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
