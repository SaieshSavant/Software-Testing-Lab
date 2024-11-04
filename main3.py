import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropDownGoogleTest:
    def setUp(self):
        self.driver = webdriver.Firefox()  
        self.driver.get("http://www.schools9.com/kdiploma11022011.htm")
        time.sleep(3)  # Wait for the page to load

    def test_dropdown(self):
        driver = self.driver
        
        select = Select(driver.find_element(By.NAME, "course"))
        options = [option.text for option in select.options]
        excel_file = "Dropdownvalues.xlsx"
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Dropdown Options"
        ws.append(["Options in drop down"]) 
        
        for option in options:
            ws.append([option])  
        
        wb.save(excel_file)
        print(f"Dropdown options saved in {excel_file}")

        text_file = "Dropdownvalues.txt"
        with open(text_file, "w") as file:
            file.write("Options in drop down\n")
            for option in options:
                file.write(option + "\n")
        
        print(f"Dropdown options saved in {text_file}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    test = DropDownGoogleTest()
    test.setUp()
    test.test_dropdown()
    test.tearDown()
