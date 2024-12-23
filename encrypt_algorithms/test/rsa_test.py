import unittest

from encrypt_algorithms import generate_keys, decrypt, encrypt, extended_gcd, modular_inverse, is_prime, mod_exp

class TestRSA(unittest.TestCase):
    def test_extended_gcd(self):
        # Проверка вычислений НОД и коэффициентов
        self.assertEqual(extended_gcd(30, 12), (6, 1, -2))
        self.assertEqual(extended_gcd(101, 103), (1, 51, -50))

    def test_modular_inverse(self):
        # Проверка модульного обратного
        self.assertEqual(modular_inverse(3, 26), 9)
        self.assertEqual(modular_inverse(7, 40), 23)

        with self.assertRaises(ValueError):
            modular_inverse(2, 4)  # Обратного элемента нет

    def test_is_prime(self):
        # Проверка простоты чисел
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(100))

    def test_mod_exp(self):
        self.assertEqual(mod_exp(2, 3, 5), 3)
        self.assertEqual(mod_exp(3, 4, 7), 4)
        self.assertEqual(mod_exp(10, 100, 13), 3)

    def test_key_generation(self):
        public_key, private_key = generate_keys()
        e, n = public_key
        d, _ = private_key

        self.assertGreater(e, 1)
        self.assertGreater(d, 1)
        self.assertGreater(n, 1)

    def test_encrypt_decrypt(self):

        public_key, private_key = generate_keys()
        message = "Hello Rudn!"

        encrypted = encrypt(public_key, message)
        decrypted = decrypt(private_key, encrypted)

        self.assertEqual(message, decrypted)

    def test_large_message(self):
        public_key, private_key = generate_keys()
        message = "Rudn " * 50

        encrypted = encrypt(public_key, message)
        decrypted = decrypt(private_key, encrypted)

        self.assertEqual(message, decrypted)


if __name__ == "__main__":
    unittest.main()
