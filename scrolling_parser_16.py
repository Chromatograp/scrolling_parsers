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

# Скрипт автоматически вставляет лайки в комментарии сайта и собирает появившиеся числа, на выходе выдает сумму чисел:

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/7/7.5/index.html")
        container = browser.find_element(By.ID, 'container')
        last_height = browser.execute_script("return arguments[0].scrollHeight;", container)
        numbers = []
        while True:
            browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", container)
            time.sleep(2)
            new_height = browser.execute_script("return arguments[0].scrollHeight", container)
            if new_height == last_height:
                break
            last_height = new_height
        box = container.find_elements(By.CLASS_NAME, 'card')
        for i in box:
            browser.execute_script("arguments[0].scrollIntoView(true);", i)
            i.find_element(By.CLASS_NAME, 'like-btn').click()
            number = i.find_element(By.CLASS_NAME, 'big-number').text
            numbers.append(number)
        print(sum([int(i) for i in numbers if i.isdigit()]))
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()