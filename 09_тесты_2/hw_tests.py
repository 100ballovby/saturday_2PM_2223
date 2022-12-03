import unittest
from hw import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.empl = Employee('Erick', 'Hershire', 3750)

    def test_give_default_raise(self):
        self.empl.give_raise()
        self.assertEqual(self.empl.salary, 8750)

    def test_give_custom_amount(self):
         self.empl.give_raise(1000)
         self.assertEqual(self.empl.salary, 4750)
