#Count Elements
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Exp8Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.get("http://www.google.co.in")
        self.driver.maximize_window()
    
    def test_count_elements(self):
        driver = self.driver
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"TOTAL NO OF LINKS = {len(links)}")

        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"TOTAL NO OF BUTTONS = {len(buttons)}")

        input_fields = driver.find_elements(By.TAG_NAME, "input")
        print(f"TOTAL NO OF INPUT FIELDS = {len(input_fields)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
