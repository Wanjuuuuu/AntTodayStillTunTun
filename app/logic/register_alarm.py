REGISTER_LIMIT_PER_USER = 20


def is_registered_more_than_limit(registered_list):
    return len(registered_list) >= REGISTER_LIMIT_PER_USER


def get_registered_stocks_of_user(user):
    return []


def is_already_registered(stock, registered_list):
    return stock in registered_list
