import unittest
from package1.TC_LoginTest import LoginTest
from package1.TC_SignupTest import SignupTest
from package2.TC_Payment import Payment
from package2.TC_PaymentReturn import PaymentReturn

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)
tc4=unittest.TestLoader().loadTestsFromTestCase(Payment)

sanity_test=unittest.TestSuite([tc2,tc1])
unittest.TextTestRunner().run(sanity_test)