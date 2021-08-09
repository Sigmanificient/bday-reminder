from src.security import sha512
import unittest

right = 'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db' \
        '27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff'


class HashTestCase(unittest.TestCase):
    def test_sha_512(self):
        self.assertEqual(sha512('test'), right)


if __name__ == '__main__':
    unittest.main()
