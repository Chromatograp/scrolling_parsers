from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Скрипт демонстрирует прокрутку страницы до нужного элемента

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/7/7.4.1/index.html")
        actions = ActionChains(browser)
        while True:
            try:
                container = browser.find_element(By.CLASS_NAME, 'step-container').find_element(By.CLASS_NAME, 'countdown')
                if container.is_displayed():
                    time.sleep(3)
                    code = container.text[5:]
                    break
            except Exception:
                pass
            actions.scroll_by_amount(1, 500).perform()
        while True:
            try:
                input_str = browser.find_element(By.TAG_NAME, 'input')
                button = browser.find_element(By.TAG_NAME, 'button')
                if input_str.is_displayed():
                    input_str.send_keys(code)
                    time.sleep(5)
                    button.click()
                    time.sleep(2)
                    print(browser.find_element(By.ID, 'final-key').text)
                    break
            except Exception:
                pass
            action = ActionChains(browser)
            action.scroll_by_amount(1, 500).perform()
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()