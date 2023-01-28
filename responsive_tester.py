import time
from math import ceil
from utils import set_path

SIZES = [480, 960, 1280, 1960]


class ResponsiveTester:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def make_screenshots(self):
        self.browser.maximize_window()
        browser_height = self.browser.get_window_size()['height']
        path = set_path(self.url)

        for size in SIZES:
            self.browser.set_window_size(size, browser_height)
            self.browser.execute_script(f'window.scrollTo(0, 0)')
            time.sleep(2)
            scroll_height = self.browser.execute_script('return document.body.scrollHeight')
            sections = ceil(scroll_height / browser_height)
            for section in range(sections):
                self.browser.execute_script(f'window.scrollTo(0, arguments[0])', section * browser_height)
                time.sleep(2)
                self.browser.save_screenshot(f'screenshots/{path}/{size}_{section}.png')

    def finish(self):
        self.browser.quit()
