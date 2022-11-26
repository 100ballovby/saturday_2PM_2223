import unittest
from name_func import get_formatted_name


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        f_n = get_formatted_name('Andrew', 'Pekarskiy')
        self.assertEqual(f_n, 'Andrew Pekarskiy')
        """сравни значения get_formatted_name и 
        Andrew Pekarskiy, если они полностью совпадают - ок,
        если нет, скажи мне об этом."""
    def test_first_middle_last_name(self):
        f_n = get_formatted_name('Andrew', 'Pekarskiy', 'Johnsovich')
        self.assertEqual(f_n, 'Andrew Johnsovich Pekarskiy')

if __name__ == '__main__':
    unittest.main()