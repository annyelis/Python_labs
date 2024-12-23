import unittest
from encrypt_algorithms import (
    Gronsfeld_encrypt,
    Gronsfeld_decrypt,
    Gronsfeld_generate_key,
)


class TestGronsfeldCipher(unittest.TestCase):
    def test_encrypt_uppercase(self):
        self.assertEqual(Gronsfeld_encrypt("HELLO", 123), "IGOMQ")

    def test_encrypt_lowercase(self):
        self.assertEqual(Gronsfeld_encrypt("hello", 123), "igomq")

    def test_encrypt_mixed_case(self):
        self.assertEqual(Gronsfeld_encrypt("HelloWorld", 321), "KgmoqXrtmg")

    def test_encrypt_with_punctuation(self):
        self.assertEqual(Gronsfeld_encrypt("Hello, World!", 123), "Igomq, Zptoe!")

    def test_encrypt_invalid_characters(self):
        with self.assertRaises(ValueError):
            Gronsfeld_encrypt("Hello@World", 123)

    def test_decrypt_uppercase(self):
        self.assertEqual(Gronsfeld_decrypt("IGOMQ", 123), "HELLO")

    def test_decrypt_lowercase(self):
        self.assertEqual(Gronsfeld_decrypt("igomq", 123), "hello")

    def test_decrypt_mixed_case(self):
        self.assertEqual(Gronsfeld_decrypt("KgmoqXrtmg", 321), "HelloWorld")

    def test_decrypt_with_punctuation(self):
        self.assertEqual(Gronsfeld_decrypt("Igomq, Zptoe!", 123), "Hello, World!")

    def test_decrypt_invalid_characters(self):
        with self.assertRaises(ValueError):
            Gronsfeld_decrypt("Igomq@Wosle", 123)

    def test_round_trip(self):
        original_message = "Gronsfeld Cipher Test."
        key = 56789
        encrypted = Gronsfeld_encrypt(original_message, key)
        decrypted = Gronsfeld_decrypt(encrypted, key)
        self.assertEqual(decrypted, original_message)

    def test_generate_key_length(self):
        key_length = 10
        key = Gronsfeld_generate_key(key_length)
        self.assertEqual(len(key), key_length)

    def test_generate_key_numeric(self):
        key = Gronsfeld_generate_key(15)
        self.assertTrue(all(char.isdigit() for char in key))


if __name__ == "__main__":
    unittest.main()
