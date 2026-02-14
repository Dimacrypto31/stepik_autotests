import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    xelement = browser.find_element(By.XPATH, '//*[contains(@id, "input_value")]')
    x = xelement.text

    y = calc(x)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    option1 = browser.find_element(By.XPATH, '//*[contains(@id, "robotCheckbox")]')
    option1.click()
    option1 = browser.find_element(By.XPATH, '//*[contains(@id, "robotsRule")]')
    option1.click()

    button = browser.find_element(By.XPATH, '//*[contains(@type, "submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
