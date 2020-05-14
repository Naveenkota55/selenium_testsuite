import unittest

class LoginTest(unittest.TestCase):
    def test_twitter(self):
        print("This is login by twitter")
        self.assertTrue(True)
    def test_facebook(self):
        print("this is login by facebook")
        self.assertTrue(True)
    def test_apple(self):
        print("this is login by apple")
        self.assertTrue(True) 
if __name__=="__main__":
    unittest.main()