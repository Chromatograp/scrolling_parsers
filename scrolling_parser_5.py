# Импорт модуля webdriver из библиотеки Selenium для управления браузером
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Скрипт демонстрирует нажатие клавиш после открытия сайта

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/7/7.3.3/index.html")
        actions = ActionChains(browser)
        actions.key_down(Keys.CONTROL) \
            .key_down(Keys.ALT) \
            .key_down(Keys.SHIFT) \
            .key_down('T') \
            .perform()
        actions.key_up(Keys.CONTROL) \
            .key_up(Keys.ALT) \
            .key_up(Keys.SHIFT) \
            .key_up('T') \
            .perform()
        print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()