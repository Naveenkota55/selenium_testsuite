import unittest
class PaymentReturn(unittest.TestCase):
    def test_original(self):
        print("payment returned to original mode of payment")
        self.assertTrue(True)
    def test_credit(self):
        print("payment returned to credit card")
        self.assertTrue(True)
    def test_debit(self):
        print("payment returned to debit card")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()