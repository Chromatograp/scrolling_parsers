from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_argument('--dns-prefetch-disable')

# Скрипт демонстрирует поочередное нажатие и удерживание кнопок веб-страницы:

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/5.7/5/index.html")
        actions = ActionChains(browser)
        for x in range(4):
            button = browser.find_element(By.ID, f'button{x+1}')
            hold_time = button.get_attribute('value')
            actions.click_and_hold(button).pause(float(hold_time)).release(button).perform()
        print(browser.switch_to.alert.text)
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()