import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):

        emp_1 = Employee('Otman', 'Andour', 50000)
        emp_2 = Employee('Test', 'User', 60000)

        self.assertEqual(emp_1.email, 'Otman.Andour@company.com')
        self.assertEqual(emp_2.email, 'Test.User@company.com')

        emp_1.first = 'Deku'
        emp_2.first = 'Katchan'

        self.assertEqual(emp_1.email, 'Deku.Andour@company.com')
        self.assertEqual(emp_2.email, 'Katchan.User@company.com')

    def test_full_name(self):

        emp_1 = Employee('Otman', 'Andour', 50000)
        emp_2 = Employee('Test', 'User', 60000)

        self.assertEqual(emp_1.full_name, 'Otman Andour')
        self.assertEqual(emp_2.full_name, 'Test User')

        emp_1.first = 'Deku'
        emp_2.first = 'Katchan'

        self.assertEqual(emp_1.full_name, 'Deku Andour')
        self.assertEqual(emp_2.full_name, 'Katchan User')

    def test_apply_raise(self):

        emp_1 = Employee('Otman', 'Andour', 50000)
        emp_2 = Employee('Test', 'User', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == "__main__":
    unittest.main()
