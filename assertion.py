#following script contains the assert commands
import unittest
from selenium import webdriver
import time

class assert_1(unittest.TestCase):
    def test_google(self):
        self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("https://www.google.com/")
        webtitle=self.driver.title
        self.assertEqual("Google",webtitle,"webtitle not equal")#check if the webtitle is same
        self.driver.close()
if __name__=="__main__":
    unittest.main()        