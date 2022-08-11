import unittest
from employee_info import Employee

class TestEmployeeGivenRaise(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create an employee for use in all test methods."""
        self.test_employee = Employee('ethan', 'zhang', 100000)

    def test_give_default_raise(self):
        """Test if salary is raised by the default amount, $5_000."""
        self.assertEqual(self.test_employee.give_raise()[2], 105000)

    def test_give_custom_raise(self):
        """Test if salary is raised by the custom amount given."""
        self.assertEqual(self.test_employee.give_raise(3000)[2], 103000)

if __name__ == '__main__':
    unittest.main()