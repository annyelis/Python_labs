import unittest
from encrypt_algorithms import caesar_cipher, caesar_decipher

class TestCaesarCipher(unittest.TestCase):

    def test_caesarCipher_simple(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")
        self.assertEqual(caesar_cipher("ABC", 3), "DEF")
        self.assertEqual(caesar_cipher("aBc XyZ", 2), "cDe ZaB")
        self.assertEqual(caesar_cipher("Hello, Rudn!", 5), "Mjqqt, Wzis!")

    def test_caesarCipher_with_negative_shift(self):
        self.assertEqual(caesar_decipher("def", 3), "abc")
        self.assertEqual(caesar_decipher("DEF", 3), "ABC")

    def test_caesarCipher_non_alpha(self):
        self.assertEqual(caesar_cipher("Hello Rudn123!", 3), "Khoor Uxgq123!")

    def test_caesarCipher_cyrillic_error(self):
        with self.assertRaises(ValueError):
            caesar_cipher("Тест", 3)

        with self.assertRaises(ValueError):
            caesar_cipher("Hello, рудн!", 3)

    def test_caesarCipher_empty(self):
        self.assertEqual(caesar_cipher("", 3), "")


if __name__ == '__main__':
    unittest.main()