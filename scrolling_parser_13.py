from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_argument('--dns-prefetch-disable')

# Скрипт демонстрирует сбор элементов из разных частей веб-страницы:

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/5.7/1/index.html")
        while True:
            try:
                alert = WebDriverWait(browser, 1).until(EC.alert_is_present())
                if alert:
                    print(browser.switch_to.alert.text)
                    break
            except Exception as e:
                button = browser.find_element(By.TAG_NAME, 'button')
                browser.execute_script("return arguments[0].scrollIntoView(true);", button)
                button.click()

    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()