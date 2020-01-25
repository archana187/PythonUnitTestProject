import unittest

from selenium import webdriver

class SearchEngines(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="E:\WebDrivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of google page:" + self.driver.title)

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="E:\WebDrivers\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of Bing page:" + self.driver.title)

if __name__ == "__main__":
    unittest.main()