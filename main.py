from common.browser import Browser
from features.google_searching_screenshot import GoogleSearchingScreenshot
from features.responsive_tester import ResponsiveTester

google_browser = Browser('https://www.google.com').get_browser()

# study_searcher = GoogleSearchingScreenshot(google_browser, 'how to learn python', 'screenshots')
# study_searcher.get_screenshots()

ts_searcher = GoogleSearchingScreenshot(google_browser, 'typescript')
ts_searcher.get_screenshots()

nomad_browser = Browser('https://nomadcoders.co').get_browser()
ui_tester = ResponsiveTester(nomad_browser, 'https://nomadcoders.co')
ui_tester.make_screenshots()
