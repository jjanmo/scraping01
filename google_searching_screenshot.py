from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec


class GoogleSearchingScreenshot:
    def __init__(self, keyword, storage_path):
        self.keyword = keyword
        self.storage_path = storage_path
        self.browser = self.__set_browser()

    def __set_browser(self):
        options = Options()
        options.add_experimental_option("detach", True)  # prevent auto-Off
        browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        browser.get('https://www.google.com')

        return browser

    def get_screenshots(self):
        search_bar = self.browser.find_element(By.CLASS_NAME, 'gLFyf')  # select google input
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        # noinspection PyBroadException
        try:
            except_element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.CLASS_NAME, 'cUnQKe')))
            self.browser.execute_script(
                'const element = arguments[0]; element.parentElement.remove();',
                except_element
            )
            except_element = self.browser.find_element(By.CLASS_NAME, 'EyBRub')
            self.browser.execute_script(
                'const element = arguments[0]; element.parentElement.remove();',
                except_element
            )
        except Exception:
            pass

        results = self.browser.find_elements(By.CSS_SELECTOR, '#search .MjjYud')

        for index, result in enumerate(results):
            result.screenshot(f'{self.storage_path}/{self.keyword}_{index}.png')

    def quit(self):
        self.browser.quit()
