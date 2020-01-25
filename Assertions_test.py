import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testAssertions(self):
        driver=webdriver.Chrome(executable_path="E:\WebDrivers\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage=driver.title

        #assertEqual  asserNotEqual()
        #self.assertEqual( titleOfWebPage,"Google","webpage title is not working...")
        #self.assertNotEqual(titleOfWebPage, "Google123", "webpage title is  working...")


       #assertTrue()   assertFalse()

        #self.assertTrue(titleOfWebPage=="Google")  #test case passed
        self.assertFalse(titleOfWebPage == "Google1223")


if __name__=="__main__":
    unittest.main()