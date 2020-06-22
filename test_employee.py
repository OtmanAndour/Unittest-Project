import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Otman', 'Andour', 50000)
        self.emp_2 = Employee('Test', 'User', 60000)

    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Otman.Andour@company.com')
        self.assertEqual(self.emp_2.email, 'Test.User@company.com')

        self.emp_1.first = 'Deku'
        self.emp_2.first = 'Katchan'

        self.assertEqual(self.emp_1.email, 'Deku.Andour@company.com')
        self.assertEqual(self.emp_2.email, 'Katchan.User@company.com')

    def test_full_name(self):

        self.assertEqual(self.emp_1.full_name, 'Otman Andour')
        self.assertEqual(self.emp_2.full_name, 'Test User')

        self.emp_1.first = 'Deku'
        self.emp_2.first = 'Katchan'

        self.assertEqual(self.emp_1.full_name, 'Deku Andour')
        self.assertEqual(self.emp_2.full_name, 'Katchan User')

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Andour/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/User/June')
            self.assertEqual(schedule, 'Bad Response.')


if __name__ == "__main__":
    unittest.main()
