"""A module with functions to test text translation from english to french and vice-versa"""
import unittest

from translator import english_french, french_english

class TestEnglish(unittest.TestCase):
    """A class to tests translation"""
    def test_eng2french(self):
        """A function to test text translation from english to french."""
        self.assertEqual(english_french('Hello'),'Bonjour')
        self.assertNotEqual(english_french('Goodbye'), 'Bonjour')

class TestFrench(unittest.TestCase):
    """A class to tests translation"""
    def test_french2eng(self):
        """A function to test text translation from french to english."""
        self.assertEqual(french_english('Bonjour'),'Hello')
        self.assertNotEqual(french_english('Au revoir'), 'Hello')
