import unittest
class SignupTest(unittest.TestCase):
    def test_twitter(self):
        print("This is signup by twitter")
        self.assertTrue(True)
    def test_facebook(self):
        print("this is signup by facebook")
        self.assertTrue(True)
    def test_apple(self):
        print("this is signup by apple")
        self.assertTrue(True)
    
if __name__=="__main__":
    unittest.main()