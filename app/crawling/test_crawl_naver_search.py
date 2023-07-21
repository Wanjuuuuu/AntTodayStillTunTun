import unittest
from crawl_naver_search import *


class CrawlNaverSearchCase(unittest.TestCase):
    def test_crawl_stock_price_in_naver(self):
        stock_info = crawl_stock_info_in_naver('카카오')
        self.assertEqual(stock_info['name'], '카카오')
        self.assertTrue(isinstance(stock_info['price'], float))
        self.assertTrue(isinstance(stock_info['time'], str))


if __name__ == '__main__':
    unittest.main()
