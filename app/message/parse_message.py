from math import inf

CANCEL_MESSAGE = '취소'
RANGE_SEPARATOR = '~'


class Message:
    def __init__(self, content):
        self.content = content


class CancelMessage(Message):
    def __init__(self):
        super().__init__(CANCEL_MESSAGE)


class InvalidMessage(Message):
    def __init__(self):
        super().__init__('')


class StockNameMessage(Message):
    def __init__(self, stock_name):
        super().__init__(stock_name)


class StockPriceRangeMessage(Message):
    def __init__(self, lower_bound, upper_bound):
        super().__init__('')
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound


def parse_stock_name(message):
    if CANCEL_MESSAGE in message:
        return CancelMessage()
    # TODO: validate stock name
    return StockNameMessage(message)


def parse_stock_price_range(message):
    if CANCEL_MESSAGE in message:
        return CancelMessage()
    if RANGE_SEPARATOR not in message:
        return InvalidMessage()

    bounds = message.split(RANGE_SEPARATOR)
    if len(bounds) != 2:
        return InvalidMessage()

    if bounds[0] == '' and bounds[1] == '':
        return InvalidMessage()

    lower_bound = parse_float(bounds[0])
    upper_bound = parse_float(bounds[1])
    if bounds[0] == '':
        lower_bound = 0
    if bounds[1] == '':
        upper_bound = inf

    if lower_bound < 0 or upper_bound < 0:
        return InvalidMessage()
    if lower_bound > upper_bound:
        return InvalidMessage()
    return StockPriceRangeMessage(lower_bound, upper_bound)


def parse_float(s):
    try:
        s = ''.join(s.split(','))
        return float(s)
    except ValueError:
        return -1
