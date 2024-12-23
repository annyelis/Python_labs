import unittest
from string import ascii_letters
from encrypt_algorithms import Vigenere_encrypt, Vigenere_decrypt, Vigenere_generate_key

class TestVigenereCipher(unittest.TestCase):

    def test_encrypt_decrypt(self):
        message = "Hello, World!"
        key = "Key"
        encrypted = Vigenere_encrypt(message, key)
        decrypted = Vigenere_decrypt(encrypted, key)
        self.assertEqual(decrypted, message, "Дешифрованное сообщение не совпадает с оригиналом")

    def test_preserve_case(self):
        message = "HelloWorld"
        key = "Key"
        encrypted = Vigenere_encrypt(message, key)
        self.assertTrue(encrypted.isupper() == message.isupper() and encrypted.islower() == message.islower(),
                        "Шифрование не сохраняет регистр текста")
        decrypted = Vigenere_decrypt(encrypted, key)
        self.assertEqual(decrypted, message, "Дешифрование не сохраняет регистр текста")

    def test_non_alpha_characters(self):
        message = "1234, test!@#"
        key = "Key"
        encrypted = Vigenere_encrypt(message, key)
        self.assertEqual(encrypted[:5], message[:5], "Неалфавитные символы были изменены")
        decrypted = Vigenere_decrypt(encrypted, key)
        self.assertEqual(decrypted, message, "Дешифрование неверно обработало неалфавитные символы")

    def test_generate_key(self):
        length = 10
        key = Vigenere_generate_key(length)
        self.assertEqual(len(key), length, "Сгенерированный ключ имеет неправильную длину")
        self.assertTrue(all(char in ascii_letters for char in key),
                        "Сгенерированный ключ содержит недопустимые символы")

    def test_empty_message(self):
        message = ""
        key = "Key"
        encrypted = Vigenere_encrypt(message, key)
        decrypted = Vigenere_decrypt(encrypted, key)
        self.assertEqual(decrypted, message, "Обработка пустого сообщения работает некорректно")

    def test_empty_key(self):
        message = "Hello, World!"
        key = ""
        with self.assertRaises(ZeroDivisionError):
            Vigenere_encrypt(message, key)

    def test_full_cycle(self):
        for _ in range(10):
            message = Vigenere_generate_key(20)
            key = Vigenere_generate_key(5)
            encrypted = Vigenere_encrypt(message, key)
            decrypted = Vigenere_decrypt(encrypted, key)
            self.assertEqual(decrypted, message, "Дешифрование не восстановило случайное сообщение")

if __name__ == "__main__":
    unittest.main()
