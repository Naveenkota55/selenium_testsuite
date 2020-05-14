import unittest

class Payment(unittest.TestCase):
    def test_cash(self):
        print("Transation through cash")
        self.assertTrue(True)
    def test_card_credit(self):
        print("Transation through credit card")
        self.assertTrue(True)
    def test_card_Debit(self):
        print("Transaction through Debit")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()