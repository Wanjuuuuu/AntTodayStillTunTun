import unittest
from register_alarm import *


class RegisterAlarmCase(unittest.TestCase):
    STOCK = '카카오'
    USER = '유저'

    def test_kakao_is_not_registered_yet(self):
        registered_stocks = []
        already_registered = is_already_registered(self.STOCK, registered_stocks)
        self.assertEqual(already_registered, False)

    def test_kakao_is_already_registered(self):
        registered_stocks = [self.STOCK]
        already_registered = is_already_registered(self.STOCK, registered_stocks)
        self.assertEqual(already_registered, True)

    def test_can_register_stock(self):
        registered_stocks = []
        more_than_limit = is_registered_more_than_limit(registered_stocks)
        self.assertEqual(more_than_limit, False)

    def test_is_already_registered_equal_to_limit(self):
        registered_stocks = []
        for i in range(REGISTER_LIMIT_PER_USER):
            registered_stocks.append('')
        more_than_limit = is_registered_more_than_limit(registered_stocks)
        self.assertEqual(more_than_limit, True)


if __name__ == '__main__':
    unittest.main()
