import unittest
import func_annexe
from readcsv import readcsv

"""Ce script test
    les fonctions """


class TestApp(unittest.TestCase):
    def test_readcsv(self):
        self.assertIsInstance(type(readcsv()), type)
        self.assertIsNotNone(readcsv())

    def test_allcountry(self):
        self.assertIs(type(func_annexe.allcountries()), list)
        self.assertIs(type(func_annexe.allcountries()[0]), str)
        self.assertNotEqual(func_annexe.allcountries(), [])

    def test_bycountry(self):
        self.assertIs(type(func_annexe.bycountry("Cameroon")), dict)
        self.assertEqual(
            func_annexe.bycountry("Cameroon"),
            {'Country': 'Cameroon', 'Year': 2017, 'Emissions': 6152.919})
        self.assertEqual(
            func_annexe.bycountry("Serbia"),
            {'Country': 'Serbia', 'Year': 2017, 'Emissions': 46129.569})

    def test_allyears(self):
        self.assertIs(type(func_annexe.allyears()), list)
        self.assertEqual(
            func_annexe.allyears(),
            [1975, 1985, 1995, 2005, 2010, 2015, 2016, 2017])

    def test_byyear(self):
        self.assertIs(type(func_annexe.byyear(1995)), dict)
        self.assertEqual(
            func_annexe.byyear(1995),
            {"Year": 1995, "Total": 150541.976})
        self.assertEqual(
            func_annexe.byyear(2010),
            {"Year": 2010, "Total": 207976.702})

    def test_bypercapita(self):
        self.assertIs(type(func_annexe.bypercapita('Cameroon')), dict)
        self.assertEqual(
            func_annexe.bypercapita('Cameroon'),
            {1975: 0.137, 1985: 0.237, 1995: 0.183, 2005: 0.169,
             2010: 0.253, 2015: 0.26, 2016: 0.26, 2017: 0.256})
        self.assertEqual(
            func_annexe.bypercapita('Yemen'),
            {1975: 0.257, 1985: 0.493, 1995: 0.616, 2005: 0.915,
             2010: 0.948, 2015: 0.433, 2016: 0.34, 2017: 0.316})


if __name__ == '__main__':
    unittest.main()
