from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) #ждет 12 сек, пока текст не будет равен 100$
    browser.find_element(By.XPATH, '//*[contains(@id, "book")]').click()

    browser.execute_script("window.scrollBy(0, 350);")

    xelem = browser.find_element(By.XPATH, '//*[contains(@id, "input_value")]')
    x = xelem.text
    y = calc(x)

    input = browser.find_element(By.XPATH, '//*[contains(@class, "form-control")]')
    input.send_keys(y)

    browser.find_element(By.XPATH, '//*[contains(@type, "submit")]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
