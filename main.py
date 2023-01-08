from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)  # prevent auto-Off
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get('https://google.com')
