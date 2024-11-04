import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Exp8Test(unittest.TestCase):
    
    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Firefox()  # Make sure to have the GeckoDriver installed for Firefox
        self.driver.get("http://www.google.co.in")
        self.driver.maximize_window()
    
    def test_count_elements(self):
        driver = self.driver
        
        # Get all links on the page
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"TOTAL NO OF LINKS = {len(links)}")
        
        # Get all buttons on the page
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"TOTAL NO OF BUTTONS = {len(buttons)}")
        
        # Get all input fields on the page
        input_fields = driver.find_elements(By.TAG_NAME, "input")
        print(f"TOTAL NO OF INPUT FIELDS = {len(input_fields)}")
    
    def tearDown(self):
        # Stop the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
