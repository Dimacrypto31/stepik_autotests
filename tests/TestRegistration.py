import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("ivan@example.com")

        # Нажимаем кнопку
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем результат
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!"
        )

        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля (здесь будет ошибка)
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("ivan@example.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!"
        )

        browser.quit()

        #Чтобы получить ответ в PyCharm, в его терминале введите: python -m unittest {test}.py (Ответом будет предпоследняя строка, содержащая ошибку)


if __name__ == "__main__":
    unittest.main()
