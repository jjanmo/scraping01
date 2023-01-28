from browser import Browser
from google_searching_screenshot import GoogleSearchingScreenshot
from responsive_tester import ResponsiveTester

google_browser = Browser('https://www.google.com').get_browser()

# study_searcher = GoogleSearchingScreenshot(google_browser, 'how to learn python', 'screenshots')
# study_searcher.get_screenshots()
# study_searcher.quit()

ts_searcher = GoogleSearchingScreenshot(google_browser, 'typescript', 'screenshots')
ts_searcher.get_screenshots()
ts_searcher.quit()

# nomad_browser = Browser('https://nomadcoders.co').get_browser()
# ui_tester = ResponsiveTester(nomad_browser, 'https://nomadcoders.co')
# ui_tester.make_screenshots()
# ui_tester.finish()
