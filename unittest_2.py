import unittest
from selenium import webdriver
import time

def setUpModule():
    print("start of module")
def tearDownModule():
    print("end of module")
class searchengine(unittest.TestCase):
    driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    
    @classmethod
    def setUp(self):
        print("this is setup")

    @classmethod
    def tearDown(self):
        print("this is teardown")
    
    @classmethod
    def tearDownClass(hi):
        print("end of class")
    
    @classmethod
    def setUpClass(hi):
        print("start of class")

    def test_google(self):
        #self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("http://google.com")
        print(self.driver.title)
        self.driver.close()
        
    def test_bing(self):
        #self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("https://bing.com")
        print(self.driver.title)
     #   self.driver.close()
if __name__=="__main__":
    unittest.main()
        