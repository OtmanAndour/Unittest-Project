import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(5, -3), 8)
        self.assertEqual(calc.substract(-5, 2), -7)
        self.assertEqual(calc.substract(-6, -5), -1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(5, 0), 0)
        self.assertEqual(calc.multiply(-4, 3), -12)
        self.assertEqual(calc.multiply(-2, -5), 10)

    def test_divide(self):
        self.assertEqual(calc.divide(6, 2), 3)
        self.assertEqual(calc.divide(0, 5), 0)
        self.assertEqual(calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
