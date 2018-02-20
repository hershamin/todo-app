from django.test import TestCase
from ..misc.utils import AESCipher


class UtilsTest(TestCase):

    def setUp(self):
        self.aes = AESCipher()

    def test_string_encryption(self):
        """String can encrypt and decrypt"""
        decStr = 'decrypted string'
        encStr = self.aes.encrypt(decStr)
        dec = self.aes.decrypt(encStr)
        self.assertEqual(decStr, dec)
