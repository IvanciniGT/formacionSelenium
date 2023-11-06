from selenium import webdriver

import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() # .'\\chromedriver.exe')
        self.driver.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.find_element_by_id("txt-username").clear()
        driver.find_element_by_id("txt-username").send_keys("John Doe")
        driver.find_element_by_id("txt-password").clear()
        driver.find_element_by_id("txt-password").send_keys("ThisIsNotAPassword")
        driver.find_element_by_id("btn-login").click()
        self.assertEqual("Make Appointment", driver.find_element_by_xpath("//section[@id='appointment']/div/div/div/h2").text)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
