import time
from math import ceil
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

url = 'https://nomadcoders.co/'
options = Options()
options.add_experimental_option("detach", True)  # prevent auto-Off
browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
browser.get(url)
browser.maximize_window()

browser_height = browser.get_window_size()['height']

sizes = [480, 960, 1280, 1960]

splited = url.split('://')[1].split('.')
path = splited[0] if len(splited) == 2 else splited[1]
Path(f'screenshots/{path}').mkdir(parents=True, exist_ok=True)

for size in sizes:
    browser.set_window_size(size, browser_height)
    browser.execute_script(f'window.scrollTo(0, 0)')
    time.sleep(2)
    scroll_height = browser.execute_script('return document.body.scrollHeight')
    sections = ceil(scroll_height / browser_height)
    for section in range(sections):
        browser.execute_script(f'window.scrollTo(0, arguments[0])', section * browser_height)
        time.sleep(2)
        browser.save_screenshot(f'screenshots/{path}/{size}_{section}.png')

browser.quit()
