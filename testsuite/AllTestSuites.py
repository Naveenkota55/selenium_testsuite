#following script imports testcases from other python file created earlier 
#and create test suites and runs based on choise

import unittest             #import test cases
from package1.TC_LoginTest import LoginTest
from package1.TC_SignupTest import SignupTest
from package2.TC_Payment import Payment
from package2.TC_PaymentReturn import PaymentReturn

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)  #load testcases 
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)
tc4=unittest.TestLoader().loadTestsFromTestCase(Payment)

sanity_test=unittest.TestSuite([tc2,tc1])               #create test suite
funitional_test=unittest.TestSuite([tc3,tc4])   
master_test=unittest.TestSuite([tc1,tc2,tc3,tc4])

option=int(input("enter a OPTION  1. Sanity    2. funtional  3. Master      :"))        #choose a option fro test
if option==1:
    print("Sanity_test selected")
    unittest.TextTestRunner().run(sanity_test)
elif option==2:
    print("functional test selected")
    unittest.TextTestRunner().run(funitional_test)
elif option==3:
    print("master test selected")
    unittest.TextTestRunner(verbosity=2).run(master_test) 
else:
    print("invaild option")