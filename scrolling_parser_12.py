from selenium.webdriver.common.action_chains import ActionChains
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

# Скрипт демонстрирует прокрутку нескольких контейнеров страницы и сбор информации из одинаковых элементов

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/infiniti_scroll_3/")
        actions = ActionChains(browser)
        final_list = []

        for x in range(5):
            list_elements = []
            container = browser.find_element(By.ID, f'scroll-container_{x+1}')
            last_height = browser.execute_script("return arguments[0].scrollHeight;", container)
            while True:
                browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", container)
                time.sleep(2)
                new_height = browser.execute_script("return arguments[0].scrollHeight", container)
                if new_height == last_height:
                    break
                last_height = new_height
            number = container.find_elements(By.TAG_NAME, 'span')
            for i in number:
                    if i.get_attribute('class') == 'last-of-list':
                        final_list.append(i.text)
                        break
                    else:
                        final_list.append(i.text)
                        continue
        # Сумма всех числовых значений из элементов:
        print(f'Сумма чисел: {sum([int(i) for i in final_list if i.isdigit()])}')
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()