from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Скрипт прокручивает учебную страницу до получения элемента с паролем и выводит результат в консоль.

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/7/7.1/index.html")
        height = browser.execute_script("return document.body.scrollHeight")
        time.sleep(2)
        browser.execute_script(f"window.scrollBy(0,{height})")
        time.sleep(3)
        print(browser.find_element(By.ID, 'secret-container').text)
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()