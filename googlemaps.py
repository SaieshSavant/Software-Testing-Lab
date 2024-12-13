
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleMapsAutomation:
    def setUp(self):
        self.driver = webdriver.Chrome() 

    def search_location(self):
            self.driver.get("https://www.google.com/maps")
            time.sleep(2)
            name = str(input("Enter Location: "))
            search_input = self.driver.find_element(By.ID, 'searchboxinput')
            search_input.send_keys(name)
            time.sleep(1)  
            directions = self.driver.find_element(By.ID, 'searchbox-searchbutton')
            directions.click()
            time.sleep(5) 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    automation = GoogleMapsAutomation()
    automation.setUp()
    automation.search_location()
    automation.tearDown()
