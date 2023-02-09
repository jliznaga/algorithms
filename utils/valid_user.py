import re


def is_valid_username(username):
    regex = r'^([a-z]|[A-Z])(\w){2,23}([a-z]|[A-Z]|\d)$'
    return re.match(regex, username) is not None


assert(is_valid_username('_asas') is False)
assert(is_valid_username('u__hello_world123') is True)
assert(is_valid_username('pepe##') is False)
assert(is_valid_username('as') is False)
assert(is_valid_username('asqweqw_') is False)
