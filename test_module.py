import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):
    def test_correct_output(self):
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(result['mean'], [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0])
        self.assertEqual(result['variance'], [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667])
        self.assertEqual(result['max'], [[6, 7, 8], [2, 5, 8], 8])
        self.assertEqual(result['min'], [[0, 1, 2], [0, 3, 6], 0])
        self.assertEqual(result['sum'], [[9, 12, 15], [3, 12, 21], 36])

    def test_value_error(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])
