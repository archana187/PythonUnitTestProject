import unittest

class SignUpTest(unittest.TestCase):
    def test_SignUpEmail(self):
        print("This is SignUp by email test")
        self.assertTrue(True)

    def test_SignUpByFacebook(self):
        print("This is SignUp by facebook test")
        self.assertTrue(True)

    def test_SignUpBytwitter(self):
        print("This is SignUp by twitter test")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()