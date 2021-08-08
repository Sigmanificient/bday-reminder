import re
import unittest

from src.app import USERNAME_PATTERN, PASSWORD_PATTERN


class RegexTestCase(unittest.TestCase):

    def test_user_regex(self):
        self.validate(
            pattern=USERNAME_PATTERN,
            valides=['alex', 'hello_world', 'Lorem-Ipsum', 'Frank123'],
            invalids=['abc', 'an_user!', 'hello world']
        )

    def test_password_regex(self):
        self.validate(
            pattern=PASSWORD_PATTERN,
            valides=['8dlk9dA32%'],
            invalids=[
                'this is a way too long password to be validated !',
                'lettersOnly', '1235689', 'less_8', 'letter and space',
                'letters123', 'no uppercase letters 123'
            ]
        )

    def validate(self, pattern, valides, invalids):
        for valid in valides:
            self.assertIsNotNone(re.match(pattern, valid))

        for invalid in invalids:
            self.assertIsNone(re.match(pattern, invalid))


if __name__ == '__main__':
    unittest.main()
