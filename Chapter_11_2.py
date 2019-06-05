import unittest
# 11-3: Use test cases on a class. This is advanced stuff right here. Last problem before alien invaders.


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
