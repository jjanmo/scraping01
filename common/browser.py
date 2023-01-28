from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, url):
        options = Options()
        options.add_experimental_option("detach", True)  # prevent auto-Off
        self.browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(url)

    def get_browser(self):
        return self.browser
