import unittest

class AppTesting(unittest.TestCase):
    def test_search(self):
        print("this is search test")

    def test_advancedsearch(self):
        print("This is advanced search")

    def test_prepaidrecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidrecharge(self):
        print("This is postpaid recharge test")
        self.fail("Intensionally failing test method")
        raise Exception()

    @unittest.skipIf(1==1,"1 is always equala to 1")
    def test_loginbyfacebook(self):
        print("This is login by facebook test")

    @unittest.SkipTest
    def test_loginbytwitter(self):
        print("This is login by twitter test")

    @unittest.SkipTest
    def test_loginbygmail(self):
        print("This is login by gmail test")

if __name__=="__main__":
    unittest.main()


