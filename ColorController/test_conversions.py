import unittest
from conversions import rgb_to_hex

class TestRgbToHex(unittest.TestCase):
    def test_rgb_to_hex(self):
        self.assertEqual(rgb_to_hex(0, 0, 0), '#000000')
        self.assertEqual(rgb_to_hex(255, 255, 255), '#ffffff')
        self.assertEqual(rgb_to_hex(0, 0, 1), '#000001')
        self.assertEqual(rgb_to_hex(1, 1, 1), '#010101')
        self.assertEqual(rgb_to_hex(5, 30, 255), '#051eff')
        self.assertEqual(rgb_to_hex(5.0, 29.9999, 255), '#051eff')
        self.assertEqual(rgb_to_hex(5.0, 30.0001, 255), '#051eff')
        self.assertRaises(ValueError, rgb_to_hex, 200, -30, 100)
        self.assertWarns(UserWarning, rgb_to_hex, 200.1, 20, 90.5)
        with self.assertRaises(ValueError) as context:
            rgb_to_hex(500, 30.1, 255.01)
        self.assertTrue(
            'Inputs for red, green, and blue must be integer values between 0 and 255.'
            in str(context.exception)
        )
