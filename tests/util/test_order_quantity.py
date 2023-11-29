from unittest import TestCase

from util.order_quantity import (
    check_order_minimum_quantity,
    get_order_minimum_quantity,
    trunc_order_minimum_quantity,
)


class StringMethodsTestCase(TestCase):
    def test_get_order_minimum_quantity(self):
        with self.assertRaises(ValueError):
            get_order_minimum_quantity(-1)

        self.assertEqual(get_order_minimum_quantity(0.001), 10)
        self.assertEqual(get_order_minimum_quantity(1), 10)
        self.assertEqual(get_order_minimum_quantity(99), 10)

        self.assertEqual(get_order_minimum_quantity(100), 1)
        self.assertEqual(get_order_minimum_quantity(999), 1)
        self.assertEqual(get_order_minimum_quantity(999.999999999999), 1)

        self.assertEqual(get_order_minimum_quantity(1000), 0.1)
        self.assertEqual(get_order_minimum_quantity(5000), 0.1)
        self.assertEqual(get_order_minimum_quantity(9_999), 0.1)

        self.assertEqual(get_order_minimum_quantity(10_000), 0.01)
        self.assertEqual(get_order_minimum_quantity(10_000.11), 0.01)
        self.assertEqual(get_order_minimum_quantity(99_999), 0.01)

        self.assertEqual(get_order_minimum_quantity(100_000), 0.001)
        self.assertEqual(get_order_minimum_quantity(500_000), 0.001)
        self.assertEqual(get_order_minimum_quantity(999_999.9999), 0.001)

        self.assertEqual(get_order_minimum_quantity(1_000_000), 0.0001)
        self.assertEqual(get_order_minimum_quantity(100_000_000), 0.0001)
        self.assertEqual(get_order_minimum_quantity(1_000_000_000), 0.0001)

    def test_check_order_minimum_quantity(self):
        with self.assertRaises(ValueError):
            check_order_minimum_quantity(-0.001, 10)

        self.assertTrue(check_order_minimum_quantity(0.001, 10))
        self.assertFalse(check_order_minimum_quantity(0.001, 9))

        self.assertTrue(check_order_minimum_quantity(100, 1))
        self.assertFalse(check_order_minimum_quantity(100 - 1, 1))

        self.assertTrue(check_order_minimum_quantity(1000, 0.1))
        self.assertFalse(check_order_minimum_quantity(1000 - 1, 0.1))

        self.assertTrue(check_order_minimum_quantity(10_000, 0.01))
        self.assertFalse(check_order_minimum_quantity(10_000 - 1, 0.01))

        self.assertTrue(check_order_minimum_quantity(100_000, 0.001))
        self.assertFalse(check_order_minimum_quantity(100_000 - 1, 0.001))

        self.assertTrue(check_order_minimum_quantity(1_000_000, 0.0001))
        self.assertFalse(check_order_minimum_quantity(1_000_000 - 1, 0.0001))

    def test_trunc_order_minimum_quantity(self):
        with self.assertRaises(ValueError):
            trunc_order_minimum_quantity(-0.001, 10)

        # 100미만은 10단위
        self.assertEqual(trunc_order_minimum_quantity(0.001, 9), 0)
        self.assertEqual(trunc_order_minimum_quantity(0.001, 10.1), 10)
        self.assertEqual(trunc_order_minimum_quantity(0.001, 11), 10)
        self.assertEqual(trunc_order_minimum_quantity(0.001, 20), 20)
        self.assertEqual(trunc_order_minimum_quantity(99.9999, 1), 0)

        # 100이상~1000미만은 1단위
        self.assertEqual(trunc_order_minimum_quantity(100, 1), 1)
        self.assertEqual(trunc_order_minimum_quantity(100, 1.1), 1)
        self.assertEqual(trunc_order_minimum_quantity(999.9999, 1), 1)
        self.assertEqual(trunc_order_minimum_quantity(999.9999, 1.0001), 1)

        # 1_000이상~10_000미만은 0.1단위
        self.assertEqual(trunc_order_minimum_quantity(1_000, 0.1), 0.1)
        self.assertEqual(trunc_order_minimum_quantity(1_000, 0.10001), 0.1)
        self.assertEqual(trunc_order_minimum_quantity(9_999.9999, 0.1), 0.1)
        self.assertEqual(trunc_order_minimum_quantity(9_999.9999, 0.10001), 0.1)

        # 10_000이상~100_000미만은 0.01단위
        self.assertEqual(trunc_order_minimum_quantity(10_000, 0.01), 0.01)
        self.assertEqual(trunc_order_minimum_quantity(10_000, 0.011), 0.01)
        self.assertEqual(trunc_order_minimum_quantity(99_999.99999, 0.01), 0.01)
        self.assertEqual(trunc_order_minimum_quantity(99_999.99999, 0.011), 0.01)

        # 100_000이상~1_000_000미만은 0.001단위
        self.assertEqual(trunc_order_minimum_quantity(100_000, 0.001), 0.001)
        self.assertEqual(trunc_order_minimum_quantity(100_000, 0.0011), 0.001)
        self.assertEqual(trunc_order_minimum_quantity(999_999.999999, 0.001), 0.001)
        self.assertEqual(trunc_order_minimum_quantity(999_999.999999, 0.0011), 0.001)

        # 1_000_000이상은 0.0001단위
        self.assertEqual(trunc_order_minimum_quantity(1_000_000, 0.0001), 0.0001)
        self.assertEqual(trunc_order_minimum_quantity(1_000_000, 0.00011), 0.0001)
        self.assertEqual(trunc_order_minimum_quantity(1_000_000_000, 0.0001), 0.0001)
        self.assertEqual(trunc_order_minimum_quantity(1_000_000_000, 0.00011), 0.0001)
