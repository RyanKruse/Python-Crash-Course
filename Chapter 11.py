# This chapter examines how test cases work.
import unittest


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


# 11-3: Use test cases on a class.
class Employee():
    """The employee class model"""
    def __init__(self, first, last, salary):
        """Defines variables used throughout the class"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increase=5000):
        """Increases the salary by a given parameter; default is 5000"""
        self.salary += increase


class TestCaseEmployee(unittest.TestCase):
    """This tests the give raise method in the Employee class"""
    def setUp(self):
        """Employee data stored for multiple tests"""
        self.first = 'John'
        self.last = 'Smith'
        self.salary = 50000
        self.increase = 9000
        self.my_employee = Employee(self.first, self.last, self.salary)

    def test_give_default_raise(self):
        """Tests the give raise method without providing a parameter"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 55000)

    def test_give_custom_raise(self):
        """Tests the give raise method while providing a parameter"""
        self.my_employee.give_raise(self.increase)
        self.assertEqual(self.my_employee.salary, 59000)
