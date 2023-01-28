from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils import set_path


# more challenge
# search pagination

class GoogleSearchingScreenshot:
    def __init__(self, browser, keyword):
        self.browser = browser
        self.keyword = keyword

    def get_screenshots(self):
        path = set_path(self.keyword)
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
            result.screenshot(f'screenshots/{path}/{index}.png')

        self.quit()

    def quit(self):
        self.browser.quit()
