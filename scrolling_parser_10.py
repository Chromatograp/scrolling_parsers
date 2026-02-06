from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Скрипт демонстрирует прокрутку элемента страницы и сбор информации из одинаковых элементов

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/infiniti_scroll_1/")
        list_elements = []
        num_list = []
        actions = ActionChains(browser)
        for x in range(100):
            tags = browser.find_elements(By.TAG_NAME, 'span')
            for tag in tags:
                if tag.get_attribute('class') != 'last-of-list':
                    if tag not in list_elements:
                        browser.execute_script("arguments[0].scrollIntoView(true);", tag)
                        time.sleep(1)
                        num_list.append(tag.text)
                        list_elements.append(tag)
                else:
                    if tag not in list_elements:
                        num_list.append(tag.text)
                        list_elements.append(tag)
                        break
                    break

        # Сумма всех числовых значений из элементов:
        print(f'Сумма чисел: {sum([int(i) for i in num_list if i.isdigit()])}')
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()