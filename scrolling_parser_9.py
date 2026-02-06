from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Скрипт демонстрирует прокрутку страницы и сбор информации из одинаковых элементов

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/scroll/2/index.html")
        list_elements = []
        num_list = []
        for x in range(100):
            tags = browser.find_elements(By.CLASS_NAME, 'item')
            for tag in tags:
                if tag not in list_elements:
                    tag.find_element(By.CLASS_NAME, 'checkbox_class').send_keys(Keys.DOWN)
                    time.sleep(1)
                    tag.find_element(By.CLASS_NAME, 'checkbox_class').click()
                    time.sleep(1)
                    num = tag.find_element(By.TAG_NAME, 'span').text
                    time.sleep(1)
                    num_list.append(num)
                    list_elements.append(tag)
        # Сумма всех числовых значений из элементов:
        print(f'Сумма: {sum([int(i) for i in num_list if i.isdigit()])}')
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()