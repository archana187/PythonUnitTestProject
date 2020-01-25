import unittest

from BatchTesting.Package1.TC_LoginTest import LoginTest
from BatchTesting.Package1.TC_SignupTest import SignUpTest
from BatchTesting.Package2.TC_PaymentTest import PaymentTest
from BatchTesting.Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#Get all test methods from LoginTest,SignUpTest,PaymentTest and PaymentReturnsTest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#Creating TestSuites...
sanitytestsuite=unittest.TestSuite([tc1,tc2])
functionaltestsuite=unittest.TestSuite([tc3,tc4])
mastertestsuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

#Run the specific test suite
#unittest.TextTestRunner().run(sanitytestsuite)
#unittest.TextTestRunner().run(functionaltestsuite)
unittest.TextTestRunner().run(mastertestsuite)

