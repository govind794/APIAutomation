import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnTest import PaymentReturnTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

senityTestSuites = unittest.TestSuite([tc1, tc2])
funTestSuites = unittest.TestSuite([tc3, tc4])
masertTestSuites = unittest.TestSuite([tc1, tc2, tc3, tc4])

# unittest.TextTestRunner().run(senityTestSuites)
# unittest.TextTestRunner().run(funTestSuites)
unittest.TextTestRunner(verbosity=2).run(masertTestSuites)
