import unittest
import string

def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([chr(ord(char) + 9) for char in (message)])

    print(encrypted_message)
    return encrypted_message

class Unit_Tests(unittest.TestCase):
    def setUp(self):
        self.message = "I love bacon 86"

    def test_inputExists(self):
        self.assertIsNotNone(self.message)

    def test_inputType(self):
        self.assertIsInstance(self.message, str)

    def test_functionReturnSmth(self):
        self.assertIsNotNone(encrypt(self.message))

    def test_lenIO(self):
        self.assertEqual(len(self.message), len(encrypt(self.message)))

    def test_diffIO(self):
        self.assertNotIn(self.message, encrypt(self.message))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.message), str)

    def test_shiftedCode(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([chr(ord(char) + 9) for char in (self.message)])
        print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.message))

if __name__ == "__main__":
    unittest.main()