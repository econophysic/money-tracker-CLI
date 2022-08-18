import unittest
from main import check_credential


class TestSuite(unittest.TestCase):
    username = 'test'
    password = 'test'


    def test_new_user(self):
        msg = check_credential(self.username, self.password)
        self.assertIsNone(msg)


    def test_existed_user(self):
        msg = check_credential(self.username, self.password)
        self.assertEqual(msg, 'TEST this username is already taken')


if __name__ == '__main__':
    unittest.main()
