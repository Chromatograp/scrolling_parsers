from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Скрипт демонстрирует работу с перетаскиванием элемента в заданную область

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/7/7.3.2/index.html")
        peter = browser.find_element(By.ID, 'draggable')
        pool = browser.find_element(By.ID, 'target')
        actions = ActionChains(browser)
        actions.drag_and_drop(peter, pool).perform()
        print(browser.find_element(By.ID, 'password').text)
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()