import unittest
import register_alarm


class RegisterAlarmCase(unittest.TestCase):
    STOCK = '카카오'
    USER = '유저'

    def tearDown(self) -> None:
        register_alarm.MOCK_REGISTERED_STOCKS.clear()
        return

    def test_can_register_stock_if_kakao_already_registered(self):
        register_alarm.MOCK_REGISTERED_STOCKS.append(self.STOCK)
        can_register = register_alarm.can_register_stock(self.STOCK, self.USER)
        self.assertEqual(can_register, False)

    def test_can_register_stock_if_already_registered_equal_to_limit(self):
        for i in range(register_alarm.REGISTER_LIMIT_PER_USER):
            register_alarm.MOCK_REGISTERED_STOCKS.append('')
        can_register = register_alarm.can_register_stock(self.STOCK, self.USER)
        self.assertEqual(can_register, False)

    def test_can_register_stock(self):
        can_register = register_alarm.can_register_stock(self.STOCK, self.USER)
        self.assertEqual(can_register, True)


if __name__ == '__main__':
    unittest.main()
