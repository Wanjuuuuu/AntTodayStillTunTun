import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from app.message.parse_message import parse_float


def crawl_stock_info_in_naver(stock_name):
    driver = webdriver.Chrome()

    driver.get('https://search.naver.com/search.naver?query=' + stock_name + '+주가')

    time.sleep(1)

    elements = driver.find_elements(by=By.CLASS_NAME, value='spt_tlt')
    texts = elements[0].text.splitlines()

    stock_price = parse_float(texts[2])

    elements = driver.find_elements(by=By.CLASS_NAME, value='stk_info')
    texts = elements[0].text.splitlines()

    base_time = texts[0]

    driver.quit()

    return {'name': stock_name, 'price': stock_price, 'time': base_time}
