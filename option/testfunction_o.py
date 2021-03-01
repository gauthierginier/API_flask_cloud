import unittest
import func_annexe_o
from readcsv_o import readcsv

"""Ce script test
    les fonctions """


class TestApp(unittest.TestCase):
    def test_readcsv(self):
        self.assertIsInstance(type(readcsv('Region')), type)
        self.assertIsNotNone(readcsv('Region'))

    def test_allcountry(self):
        self.assertIs(type(func_annexe_o.allcountries()), list)
        self.assertIs(type(func_annexe_o.allcountries()[0]), str)
        self.assertNotEqual(func_annexe_o.allcountries(), [])

    def test_bycountry(self):
        self.assertIs(type(func_annexe_o.bycountry("cameroon")), dict)
        self.assertEqual(
            func_annexe_o.bycountry("cameroon"),
            {'Country': 'Cameroon', 'Year': 2017, 'Emissions': 6152.919})
        self.assertEqual(
            func_annexe_o.bycountry("serbia"),
            {'Country': 'Serbia', 'Year': 2017, 'Emissions': 46129.569})

    def test_allyears(self):
        self.assertIs(type(func_annexe_o.allyears()), list)
        self.assertEqual(
            func_annexe_o.allyears(),
            [1975, 1985, 1995, 2005, 2010, 2015, 2016, 2017])

    def test_byyear(self):
        self.assertIs(type(func_annexe_o.byyear(1995)), dict)
        self.assertEqual(
            func_annexe_o.byyear(1995),
            {"Year": 1995, "Total": 150541.976})
        self.assertEqual(
            func_annexe_o.byyear(2010),
            {"Year": 2010, "Total": 207976.702})

    def test_bypercapita(self):
        self.assertIs(type(func_annexe_o.bypercapita('cameroon')), dict)
        self.assertEqual(
            func_annexe_o.bypercapita('cameroon'),
            {1975: 0.137, 1985: 0.237, 1995: 0.183, 2005: 0.169,
             2010: 0.253, 2015: 0.26, 2016: 0.26, 2017: 0.256})
        self.assertEqual(
            func_annexe_o.bypercapita('yemen'),
            {1975: 0.257, 1985: 0.493, 1995: 0.616, 2005: 0.915,
             2010: 0.948, 2015: 0.433, 2016: 0.34, 2017: 0.316})


if __name__ == '__main__':
    unittest.main()
