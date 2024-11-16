import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(100, 21), 121)
    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-3,-2),-1)
        self.assertEqual(self.calc.subtract(15,3),12)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-6,5),-30)
        self.assertEqual(self.calc.multiply(6,5),30)
        self.assertEqual(self.calc.multiply(8,-5),-40)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5,5),1)
        self.assertEqual(self.calc.divide(-2,1),-2)
        self.assertEqual(self.calc.divide(-2,-1),2)
        self.assertEqual(self.calc.divide(2,0),"หารไม่ได้")

    def test_mod(self):
        self.assertEqual(self.calc.modulo(5,5),0)
        self.assertEqual(self.calc.modulo(-2,1),0)
        self.assertEqual(self.calc.modulo(14,-5),4)
        self.assertEqual(self.calc.modulo(2,0),"modไม่ได้")
if __name__ == '__main__':
    unittest.main()