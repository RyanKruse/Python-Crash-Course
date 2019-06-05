import unittest
# 11-1: Test a function.


def print_city_country(city, country, population=''):  # 11-1: Test a function
    """This function combines the city and country into 1 string."""
    if population:
        return city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        return city.title() + ', ' + country.title()


class TestCaseCityCountry(unittest.TestCase):
    """Tests for the city function"""

    def test_city_country(self):
        """Do names like 'santiago' and 'chile' work?"""
        formatted_city_country = print_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do names like 'santiago' and 'chile' work while including population?"""
        formatted_city_country = print_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_country, 'Santiago, Chile - population 5000000')