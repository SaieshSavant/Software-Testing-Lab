#Automate Scrolling on a Website
from selenium import webdriver
import time

class ScrollPageAutomation:
    def setUp(self):
        # Initialize the Chrome browser
        self.driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH

    def scroll_page(self):
        try:
            # Open the specified URL
            self.driver.get("https://www.ibm.com/topics/software-testing")

            # Get the total height of the page
            total_height = self.driver.execute_script("return document.body.scrollHeight")

            # Scroll down the page gradually
            for i in range(0, total_height, 10):  # Adjust the step value (10) as needed
                self.driver.execute_script(f"window.scrollTo(0, {i});")
                time.sleep(0.05)  # Wait time between scrolls (adjust as needed)

            # Final scroll to the bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for a moment to observe the final position
            time.sleep(2)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    automation = ScrollPageAutomation()
    automation.setUp()
    automation.scroll_page()
    automation.tearDown()
