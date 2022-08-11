#exercise 11-1
import unittest
from unittest import result
from city_functions import city_country

class CityFunctionsTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do pairs like 'Chengdu, China' work?"""
        result_pair = city_country('chengdu', 'china')
        self.assertEqual(result_pair, 'Chengdu, China')

    def test_city_country_population(self):
        """Do pairs like 'Chengdu, China - population 20000000' work?"""
        result_pair = city_country('chengdu', 'china', '20000000')
        self.assertEqual(result_pair, 'Chengdu, China - population 20000000')

if __name__ == '__main__':
    unittest.main()