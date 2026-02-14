from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)

    input1 = browser.find_element(By.XPATH, '//*[contains(@name, "firstname")]')
    input1.send_keys('Dima')
    input2 = browser.find_element(By.XPATH, '//*[contains(@name, "lastname")]')
    input2.send_keys('Sheplyakov')
    input3 = browser.find_element(By.XPATH, '//*[contains(@name, "email")]')
    input3.send_keys('Harad@gmail.com')

    input4 = browser.find_element(By.XPATH, '//*[contains(@name, "file")]')
    input4.send_keys(file_path)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, '//*[contains(@class, "btn btn-primary")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
