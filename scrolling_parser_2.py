from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Парсер заполняет динамически появляющиеся поля учебного сайта и возвращает в консоли пароль, который появляется в конце страницы также динамически.

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/7/7.2/index.html")
        list_input = []
        # Известно, что на сайте находится ровно 100 полей для ввода, поэтому при парсинге ориентируемся на это число:
        while len(list_input) < 100:
            elements = browser.find_elements(By.CLASS_NAME, 'interactive')
            for element in elements:
                if element not in list_input:
                    element.send_keys('text')
                    element.send_keys(Keys.ENTER)
                    element.send_keys(Keys.DOWN)
                    list_input.append(element)
        else:
            print(browser.find_element(By.ID, 'hidden-password').text)
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()