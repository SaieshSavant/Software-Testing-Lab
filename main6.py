#Browser Automation For Google Maps
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleMapsAutomation:
    def setUp(self):
        # Initialize the Chrome browser
        self.driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH

    def search_location(self):
        try:
            g_link = "https://www.google.com/maps"
            ip_link = '//*[@id="searchboxinput"]'
            directions_xpath = '//*[@id="searchbox-searchbutton"]'  # Adjusted for the correct XPath for the search button

            # Open Google Maps
            self.driver.get(g_link)
            time.sleep(2)

            # Input location from user
            name = str(input("Enter Location: "))
            search_input = self.driver.find_element(By.XPATH, ip_link)
            search_input.send_keys(name)
            time.sleep(1)  # Wait briefly to ensure input is registered

            # Click on the search button to get directions
            directions = self.driver.find_element(By.XPATH, directions_xpath)
            directions.click()
            time.sleep(5)  # Wait for the map and directions to load

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    automation = GoogleMapsAutomation()
    automation.setUp()
    automation.search_location()
    automation.tearDown()
