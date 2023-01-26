from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

KEYWORD = 'buy domain'
options = Options()
options.add_experimental_option("detach", True)  # prevent auto-Off
browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
browser.get('https://google.com')

search_bar = browser.find_element(By.CLASS_NAME, 'gLFyf')  # select google input
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

except_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cUnQKe')))
browser.execute_script(
    'const element = arguments[0]; element.parentElement.remove();',
    except_element
)
except_element = browser.find_element(By.CLASS_NAME, 'EyBRub')
browser.execute_script(
    'const element = arguments[0]; element.parentElement.remove();',
    except_element
)

results = browser.find_elements(By.CSS_SELECTOR, '#search .MjjYud')
for index, result in enumerate(results):
    result.screenshot(f'screenshots/{KEYWORD}_{index}.png')


# driver.quit()
