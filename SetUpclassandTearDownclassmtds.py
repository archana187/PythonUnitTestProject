import unittest

class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("Login to application...")

    @classmethod
    def tearDownClass(self):
        print("Logout from application...")

    def test_search(self):
        print("this is search test")

    def test_advancedsearch(self):
        print("This is advanced search")

    def test_prepaidrecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidrecharge(self):
        print("This is postpaid recharge test")


if __name__ == "__main__":
    unittest.main()
