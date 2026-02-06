from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import time

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Скрипт демонстрирует прокрутку элементов страницы

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")
        left_container = browser.find_element(By.ID, 'scrollable-container-left')
        right_container = browser.find_element(By.ID, "scrollable-container-right")
        actions = ActionChains(browser)
        actions.move_to_element(left_container).click().send_keys(Keys.END).perform()
        actions.move_to_element(right_container).click().send_keys(Keys.END).perform()
        time.sleep(10)
        print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()