
'''Test case: OrangeHRM login test
---
1)Launch browser
2) verify home page tile
3) verify login
5) close browser'''

from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="E:\WebDrivers\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title,"webpage is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed.....")

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\PythonProjects\\PythonUnitTestProject\\Reports'))
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))



