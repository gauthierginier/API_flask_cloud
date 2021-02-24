from app import allcountries
import unittest
import app

class TestApp(unittest.TestCase):
    def test_allcountry(self):
        self.assertIs(type(app.allcountries()),list)
        self.assertIs(type(app.allcountries()[0]),str)
        self.assertNotEqual(app.allcountries(),[])

    def test_bycountry(self):
        self.assertEqual(app.bycountry("Cameroon"),'{"Country": "Cameroon", "Year": 2017, "Emissions": 6152.919}')
        self.assertEqual(app.bycountry("Serbia"),'{"Country": "Serbia", "Year": 2017, "Emissions": 46129.569}')

    
    




if __name__=='__main__':
    unittest.main()