import unittest
from selenium import webdriver
import time

def setUpModule():
    print("start of module")
def tearDownModule():
    print("end of module")
class searchengine(unittest.TestCase):
    
    
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

    @unittest.SkipTest
    def test_google(self):
        self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("http://google.com")
        print(self.driver.title)
        self.driver.close()

    @unittest.skip("skipped cause test case is not completed")
    def test_bing(self):
        self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("https://bing.com")
        print(self.driver.title)
        self.driver.close()

    @unittest.skipIf(1==2,"wiki skipped")
    def test_wiki(self):
        self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("http://wikipedia.com")
        print(self.driver.title)
        self.driver.close()
    
    def test_yahoo(self):
        self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("https://yahoo.co.in")
        print(self.driver.title)
        self.driver.close()
    
    def test_duck(self):
        self.driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.get("https://duckduckgo.com/")
        print(self.driver.title)
        self.driver.close()
if __name__=="__main__":
    unittest.main()
        