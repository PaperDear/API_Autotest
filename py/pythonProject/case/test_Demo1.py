import unittest
from parameterized import parameterized

from common.read_data import load_data
from common.tools import login


class testLogin(unittest.TestCase):
    @parameterized.expand(load_data())
    def test_login(self, username, password,expect):
        self.assertEqual(expect,login(username, password))
        print(f'username:{username},password:{password},expect:{expect}')

