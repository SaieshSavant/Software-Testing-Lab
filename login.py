//login
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Exp5Test:
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://sahyadri.digital/")

    def test_login(self):
        driver = self.driver
        driver.find_element(By.ID, "student-tab").click()
        time.sleep(4) 
        driver.find_element(By.NAME, "admission_no").send_keys("admission no")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "student_pass").send_keys("password")
        time.sleep(2)
        driver.find_element(By.ID, "login-student").click()
        time.sleep(1000) 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    test = Exp5Test()
    test.setUp()
    test.test_login()
    test.tearDown()
