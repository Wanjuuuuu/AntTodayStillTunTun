REGISTER_LIMIT_PER_USER = 20
MOCK_REGISTERED_STOCKS = []


def can_register_stock(stock, user):
    registered_list = get_registered_stocks_of_user(user)
    if is_already_registered(stock, registered_list):
        return False
    if is_registered_more_than_limit(registered_list):
        return False
    return True


def get_registered_stocks_of_user(user):
    return MOCK_REGISTERED_STOCKS


def is_already_registered(stock, registered_list):
    return stock in registered_list


def is_registered_more_than_limit(registered_list):
    return len(registered_list) >= REGISTER_LIMIT_PER_USER
