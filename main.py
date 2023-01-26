from google_searching_screenshot import GoogleSearchingScreenshot

study_searcher = GoogleSearchingScreenshot('how to learn python', 'screenshots')
study_searcher.get_screenshots()
study_searcher.quit()

ts_searcher = GoogleSearchingScreenshot('typescript', 'screenshots')
ts_searcher.get_screenshots()
ts_searcher.quit()
