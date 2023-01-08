from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)  # prevent auto-Off
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get('https://google.com')

search_bar = driver.find_element(By.CLASS_NAME, 'gLFyf')
search_bar.send_keys("스쿨라이브")
search_bar.send_keys(Keys.ENTER)

search_results = driver.find_elements(By.CLASS_NAME, 'LC20lb')
results = []
for elem in search_results:
    results.append(elem.text)

print(results)

# driver.quit()
