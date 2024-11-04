#Opening and Closing Tabs in the Browser
from selenium import webdriver
import time

class BrowserAutomation:
    def setUp(self):
        self.driver = webdriver.Chrome()  

    def open_urls(self):
        try:
            url1 = "https://www.google.com/"
            url2 = "https://www.btreesystems.com/"

            # Open the first URL
            self.driver.get(url1)

            # Open a new tab and switch to it
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[1])

            # Open the second URL in the new tab
            self.driver.get(url2)

            # Wait for a moment to view the page
            time.sleep(2)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    automation = BrowserAutomation()
    automation.setUp()
    automation.open_urls()
    automation.tearDown()
