from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GoogleFormAutomation:
    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH

    def fill_form(self):
        try:
            # Open the Google Form
            self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSezs9vfDnGxHrXsF52bxKXdrmlQHbHI0HsxrO6A9PGbC3K0Xw/viewform?usp=sf_link")
            time.sleep(2)

            # Fill the Name field
            name = "Prabhu Deva"
            name_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            name_input.send_keys(name)

            # Fill the Age field
            age = "25"
            age_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            age_input.send_keys(age)

            # Fill the Email field
            email = "prabhudeva76@gmail.com"
            email_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            email_input.send_keys(email)

            # Fill the Country field
            country = "India"
            country_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
            country_input.send_keys(country)

            # Fill the City field
            city = "Chennai"
            city_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
            city_input.send_keys(city)

            # Fill the Area field
            area = "Teynampet"
            area_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
            area_input.send_keys(area)

            # Click the submit button
            submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div')
            submit.click()

            time.sleep(2)  # Wait for submission to complete

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    automation = GoogleFormAutomation()
    automation.setUp()
    automation.fill_form()
    automation.tearDown()
