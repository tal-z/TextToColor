import unittest

import pytest

from conversions import rgb_to_hex, hex_to_rgb, invert_rgb

class TestConversions(unittest.TestCase):

    def test_rgb_to_hex(self):
        self.assertEqual(rgb_to_hex(0, 0, 0), '#000000')
        self.assertEqual(rgb_to_hex(255, 255, 255), '#ffffff')
        self.assertEqual(rgb_to_hex(0, 0, 1), '#000001')
        self.assertEqual(rgb_to_hex(1, 1, 1), '#010101')
        self.assertEqual(rgb_to_hex(5, 30, 255), '#051eff')
        self.assertEqual(rgb_to_hex(5.0, 29.9999, 255), '#051eff')
        self.assertEqual(rgb_to_hex(5.0, 30.0001, 255), '#051eff')
        self.assertWarns(UserWarning, rgb_to_hex, 200.1, 20, 90.5)
        self.assertRaises(ValueError, rgb_to_hex, 200, -30, 100)
        with self.assertRaises(ValueError) as context:
            rgb_to_hex(500, 30.1, 255.01)
        self.assertTrue('Inputs for red, green, and blue must be '
                        'integer values between 0 and 255.' in str(context.exception)
                        )

    def test_hex_to_rgb(self):
        self.assertEqual(hex_to_rgb('#000000'), (0, 0, 0))
        self.assertEqual(hex_to_rgb('#FFFFFF'), (255, 255, 255))
        self.assertEqual(hex_to_rgb('0c2526'), (12, 37, 38))
        self.assertEqual(hex_to_rgb('#85d849'), (133, 216, 73))
        self.assertEqual(hex_to_rgb('2A918A'), (42, 145, 138))
        self.assertRaises(ValueError, hex_to_rgb, '2A9181b')
        self.assertRaises(ValueError, hex_to_rgb, '12345')

    def test_invert_rgb(self):
        self.assertEqual(invert_rgb(255, 255, 255), (0, 0, 0))
