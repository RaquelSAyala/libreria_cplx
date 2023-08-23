# test_complex_operations.py

import unittest
import complex_operations


class TestComplexOperations(unittest.TestCase):
    def test_add_complex(self):
        result = complex_operations.add_complex((3, 2), (-5, 5.2))
        self.assertEqual(result, (-2, 7.2))
        result = complex_operations.add_complex((0, 0), (1, -1))
        self.assertEqual(result, (1, -1))

    def test_subtract_complex(self):
        result = complex_operations.subtract_complex((3, 2), (-5, 5.2))
        self.assertEqual(result, (8, -3.2))
        result = complex_operations.subtract_complex((0, 0), (1, -1))
        self.assertEqual(result, (-1, 1))

    def test_multiply_complex(self):
        result = complex_operations.multiply_complex((3, 2), (-5, 5.2))
        self.assertEqual(result, (-17.4, -4.4))
        result = complex_operations.multiply_complex((0, 0), (1, -1))
        self.assertEqual(result, (0, 0))

    def test_divide_complex(self):
        result = complex_operations.divide_complex((3, 2), (-5, 5.2))
        self.assertAlmostEqual(result[0], -0.15426497005777178)
        self.assertAlmostEqual(result[1], -0.5825813673091445)
        result = complex_operations.divide_complex((1, 1), (1, 1))
        self.assertAlmostEqual(result[0], 1.0)
        self.assertAlmostEqual(result[1], 0.0)

    def test_modulus_complex(self):
        result = complex_operations.modulus_complex((3, 4))
        self.assertEqual(result, 5)
        result = complex_operations.modulus_complex((0, 0))
        self.assertEqual(result, 0)

    def test_conjugate_complex(self):
        result = complex_operations.conjugate_complex((3, 4))
        self.assertEqual(result, (3, -4))
        result = complex_operations.conjugate_complex((0, 0))
        self.assertEqual(result, (0, 0))

    def test_polar_to_cartesian(self):
        result = complex_operations.polar_to_cartesian((5, 0.9272952180016122))
        self.assertAlmostEqual(result[0], 3)
        self.assertAlmostEqual(result[1], 4)
        result = complex_operations.polar_to_cartesian((0, 0))
        self.assertEqual(result, (0, 0))

    def test_cartesian_to_polar(self):
        result = complex_operations.cartesian_to_polar((3, 4))
        self.assertAlmostEqual(result[0], 5)
        self.assertAlmostEqual(result[1], 0.9272952180016122)
        result = complex_operations.cartesian_to_polar((0, 0))
        self.assertEqual(result, (0, 0))

    def test_phase_complex(self):
        result = complex_operations.phase_complex((1, 1))
        self.assertAlmostEqual(result, 0.7853981633974483)
        result = complex_operations.phase_complex((1, 0))
        self.assertAlmostEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()
