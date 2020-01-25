import unittest

def setUPModule():
    print("This is setUpModule method...")

def tearDownModule():
    print("This is tearDownModule method....")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("This is setupClass method...")

    @classmethod
    def tearDownClass(self):
        print("This is tearDownClass method...")

    @classmethod
    def setUp(self):
        print("This is setUp method...")

    @classmethod
    def tearDown(self):
        print("This is tearDown method...")

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
