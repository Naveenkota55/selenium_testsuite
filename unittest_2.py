import unittest
from selenium import webdriver

class searchengine(unittest.TestCase):
    def test_bing(self):
        self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("https://www.bing.com")
        print(self.driver.title)
        self.driver.close()
    def test_google(self):
        self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("https://www.google.com")
        print(self.driver.title)
        self.driver.close()
if __name__=="__main__":
    unittest.main()