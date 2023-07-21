import unittest

from parse_message import *


class ParseMessageCase(unittest.TestCase):
    def test_parse_stock_name_if_cancel_message(self):
        message = parse_stock_name(CANCEL_MESSAGE)
        self.assertTrue(isinstance(message, CancelMessage))

    def test_parse_stock_name_if_message_contains_cancel(self):
        message = parse_stock_name('취소 카카오')
        self.assertTrue(isinstance(message, CancelMessage))

    def test_parse_stock_name(self):
        message = parse_stock_name('카카오')
        self.assertTrue(isinstance(message, StockNameMessage))

    def test_parse_stock_price_range_if_cancel_message(self):
        message = parse_stock_price_range(CANCEL_MESSAGE)
        self.assertTrue(isinstance(message, CancelMessage))

    def test_parse_stock_price_range_if_no_range_separator(self):
        message = parse_stock_price_range('10-11')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_more_than_1_separator(self):
        message = parse_stock_price_range('10~11~12')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_only_separator(self):
        message = parse_stock_price_range('~')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_two_int_bounds(self):
        message = parse_stock_price_range('10~12')
        self.assertEqual(message.lower_bound, 10)
        self.assertEqual(message.upper_bound, 12)

    def test_parse_stock_price_range_if_two_float_bounds(self):
        message = parse_stock_price_range('10.5~12.2')
        self.assertEqual(message.lower_bound, 10.5)
        self.assertEqual(message.upper_bound, 12.2)

    def test_parse_stock_price_range_if_negative_upper_bound(self):
        message = parse_stock_price_range('~-12.2')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_only_upper_bound(self):
        message = parse_stock_price_range('~12.2')
        self.assertEqual(message.lower_bound, 0)
        self.assertEqual(message.upper_bound, 12.2)

    def test_parse_stock_price_range_if_not_float_lower_bound(self):
        message = parse_stock_price_range('카카오~')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_only_lower_bound(self):
        message = parse_stock_price_range('10.5~')
        self.assertEqual(message.lower_bound, 10.5)
        self.assertEqual(message.upper_bound, inf)

    def test_parse_stock_price_range_if_inf_upper_bound(self):
        message = parse_stock_price_range('10.5~inf')
        self.assertEqual(message.lower_bound, 10.5)
        self.assertEqual(message.upper_bound, inf)

    def test_parse_stock_price_range_if_no_bounds(self):
        message = parse_stock_price_range(' ~ ')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_not_float_bound(self):
        message = parse_stock_price_range('10~카카오')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_negative_bound(self):
        message = parse_stock_price_range('-10~10')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_wrong_range(self):
        message = parse_stock_price_range('inf~10')
        self.assertTrue(isinstance(message, InvalidMessage))

    def test_parse_stock_price_range_if_int_with_comma(self):
        message = parse_stock_price_range('~10,000')
        self.assertEqual(message.lower_bound, 0)
        self.assertEqual(message.upper_bound, 10000)


if __name__ == '__main__':
    unittest.main()
