from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_argument('--dns-prefetch-disable')

# Скрипт отмечает в контейнере только чекбоксы с четным значением атрибута value:

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/5.7/4/index.html")
        container = browser.find_element(By.ID, 'main_container')
        last_height = browser.execute_script("return arguments[0].scrollHeight;", container)
        while True:
            browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", container)
            time.sleep(2)
            new_height = browser.execute_script("return arguments[0].scrollHeight", container)
            if new_height == last_height:
                break
            last_height = new_height
        box = container.find_elements(By.CLASS_NAME, 'child_container')
        for i in box:
            browser.execute_script("arguments[0].scrollIntoView(true);", i)
            checkboxes = i.find_elements(By.TAG_NAME, 'input')
            for e in checkboxes:
                if int(e.get_attribute('value')) % 2 == 0:
                    e.click()
                else:
                    pass
        browser.find_element(By.CLASS_NAME, 'alert_button').click()
        print(browser.switch_to.alert.text)
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()