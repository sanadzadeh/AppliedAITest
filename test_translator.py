import unittest
from translator import english_to_french

class TestTranslator(unittest.TestCase):
    def test_translation_equal(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

    def test_translation_not_equal(self):
        result = english_to_french("Hello")
        self.assertNotEqual(result, "Hola")

if __name__ == '__main__':
    unittest.main()
