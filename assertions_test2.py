import unittest

from selenium import webdriver

class testAssertions(unittest.TestCase):
    def testAssertions(self):
        #driver = webdriver.Chrome(executable_path="E:\WebDrivers\chromedriver.exe")
        #driver=None
        #verify the object is none or not
        #self.assertIsNone(driver)
        #self.assertIsNotNone(driver)


        list={"python","selenium","java"}
        #self.assertIn("selenium",list)
        #self.assertNotIn("selenium123",list)


        #assertions performs relational comparisions

        #self.assertGreater(100,250)
        #self.assertGreaterEqual(100, 100)

        #self.assertLess(10,100)
        self.assertLessEqual(100, 100)
