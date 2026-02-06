from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

# Скрипт демонстрирует работу с контекстным меню

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as browser:
    try:
        browser.get("https://parsinger.ru/selenium/7/7.3.4/index.html")
        button = browser.find_element(By.ID, 'context-area')
        actions = ActionChains(browser)
        actions.context_click(button).perform()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-action='get_password']"))).click()
        print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
    except TimeoutError:
        print('Страница не загрузилась')
    finally:
        browser.quit()