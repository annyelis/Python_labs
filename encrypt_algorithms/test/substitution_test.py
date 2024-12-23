import string
import unittest
from string import ascii_letters
from encrypt_algorithms import encrypt_substitution, decrypt_substitution, create_key

class TestSubstitutionCipher(unittest.TestCase):
    def test_create_key(self):
        alphabet = string.ascii_letters
        key = create_key(alphabet)
        self.assertEqual(len(key), len(alphabet))
        self.assertNotEqual(key, alphabet)

    def test_encrypt_valid_message(self):
        alphabet = string.ascii_letters
        key = create_key(alphabet)
        message = "Hello, Rudn!"
        encrypted = encrypt_substitution(message, key)
        self.assertNotEqual(encrypted, message)

    def test_decrypt_valid_message(self):
        alphabet = string.ascii_letters
        key = create_key(alphabet)
        message = "Hello, Rudn!"
        encrypted = encrypt_substitution(message, key)
        decrypted = decrypt_substitution(encrypted, key)
        self.assertEqual(decrypted, message)

    def test_encrypt_invalid_message(self):
        alphabet = string.ascii_letters
        key = create_key(alphabet)
        message = "Привет, рудн!"
        with self.assertRaises(ValueError) as context:
            encrypt_substitution(message, key)
        self.assertIn("Сообщение содержит недопустимые символы", str(context.exception))

    def test_decrypt_invalid_message(self):
        alphabet = string.ascii_letters
        key = create_key(alphabet)
        encrypted_message = "Привет, рудн!"
        with self.assertRaises(ValueError) as context:
            decrypt_substitution(encrypted_message, key)
        self.assertIn("Зашифрованное сообщение содержит недопустимые символы", str(context.exception))

    def test_encrypt_empty_message(self):
        alphabet = string.ascii_letters
        key = create_key(alphabet)
        message = ""
        encrypted = encrypt_substitution(message, key)
        self.assertEqual(encrypted, "")

    def test_decrypt_empty_message(self):
        alphabet = string.ascii_letters
        key = create_key(alphabet)
        encrypted_message = ""
        decrypted = decrypt_substitution(encrypted_message, key)
        self.assertEqual(decrypted, "")


if __name__ == "__main__":
    unittest.main()
