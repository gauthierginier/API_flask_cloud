from app import allcountries
import unittest
import app

class TestApp(unittest.TestCase):
    def test_allcountry(self):
        self.assertIs(type(app.allcountries()),list)
        self.assertIs(type(app.allcountries()[0]),str)
        self.assertNotEqual(app.allcountries(),[])

    def test_bycountry(self):
        pass




if __name__=='__main__':
    unittest.main()