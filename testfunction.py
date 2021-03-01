import unittest
import func_annexe
from readcsv import readcsv

"""Ce script test
    les fonctions """


class TestApp(unittest.TestCase):
    def test_readcsv(self):
        # on test si la sortie de la fonction test_readcsv est de type class
        self.assertIsInstance(type(readcsv('Region')), type)
        # on test que la sortie est != de None
        self.assertIsNotNone(readcsv('Region'))

    def test_allcountry(self):
        # test que la fonction retourne un liste
        # qu'elle n'est pas vide et que chaque élement est un string
        self.assertIs(type(func_annexe.allcountries()), list)
        self.assertIs(type(func_annexe.allcountries()[0]), str)
        self.assertNotEqual(func_annexe.allcountries(), [])

    def test_bycountry(self):
        # test que la fonction retourne un dictionnaire
        # test de 2 exemples
        self.assertIs(type(func_annexe.bycountry("cameroon")), dict)
        self.assertEqual(
            func_annexe.bycountry("cameroon"),
            {'Country': 'Cameroon', 'Year': 2017, 'Emissions': 6152.919})
        self.assertEqual(
            func_annexe.bycountry("serbia"),
            {'Country': 'Serbia', 'Year': 2017, 'Emissions': 46129.569})

    def test_allyears(self):
        # test que la fonction retourne une liste avec les bonnes valeurs
        self.assertIs(type(func_annexe.allyears()), list)
        self.assertEqual(
            func_annexe.allyears(),
            [1975, 1985, 1995, 2005, 2010, 2015, 2016, 2017])

    def test_byyear(self):
        # test que la fonction retourne un dictionnaire
        # test de 2 exemples
        self.assertIs(type(func_annexe.byyear(1995)), dict)
        self.assertEqual(
            func_annexe.byyear(1995),
            {"Year": 1995, "Total": 150541.976})
        self.assertEqual(
            func_annexe.byyear(2010),
            {"Year": 2010, "Total": 207976.702})

    def test_bypercapita(self):
        # test que la fonction retourne un dictionnaire
        # test de 2 exemples
        self.assertIs(type(func_annexe.bypercapita('cameroon')), dict)
        self.assertEqual(
            func_annexe.bypercapita('cameroon'),
            {1975: 0.137, 1985: 0.237, 1995: 0.183, 2005: 0.169,
             2010: 0.253, 2015: 0.26, 2016: 0.26, 2017: 0.256})
        self.assertEqual(
            func_annexe.bypercapita('yemen'),
            {1975: 0.257, 1985: 0.493, 1995: 0.616, 2005: 0.915,
             2010: 0.948, 2015: 0.433, 2016: 0.34, 2017: 0.316})


if __name__ == '__main__':
    unittest.main()
