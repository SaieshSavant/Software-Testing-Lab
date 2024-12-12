#Copy Page Details into another page
from selenium import webdriver
import time

class WebPageFetcher:
    def setUp(self):
        self.driver = webdriver.Chrome()

    def fetch_page(self):
        try:
            self.driver.get("https://www.btreesystems.com/selenium-with-python-training-in-chennai/")
            time.sleep(2)
            page_source = self.driver.page_source.encode('utf-8')

            with open('result.html', 'wb') as f:
                f.write(page_source)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def tearDown(self):   
        self.driver.quit()

if __name__ == "__main__":
    fetcher = WebPageFetcher()
    fetcher.setUp()
    fetcher.fetch_page()
    fetcher.tearDown()
