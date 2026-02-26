import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 20)

    # ОБЯЗАТЕЛЬНО открыть сайт
    browser.get("https://stepik.org")

    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    login_button.click()

    login_input = wait.until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    password_input = browser.find_element(By.ID, "id_login_password")

    login_input.send_keys("dsheplyakov@gmail.com")
    password_input.send_keys("Dim04032004a")
    password_input.send_keys(Keys.RETURN)

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.navbar__profile-img"))
    )

    yield browser
    browser.quit()


@pytest.mark.parametrize("link", links)
def test_links(browser, link):
    browser.get(link)
    wait = WebDriverWait(browser, 30)

    # ждём загрузку страницы
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    textarea = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
    )

    textarea.clear()

    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    submit_button.click()

    feedback = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
    )

    feedback_text = feedback.text

    assert feedback_text == "Correct!", \
        f'ожидался "Correct!", но получено "{feedback_text}"'