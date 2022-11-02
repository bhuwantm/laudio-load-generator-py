import random


def handle_division(n, d):
    """
    :param n: numerator
    :param d: denominator
    :return: number
    """
    try:
        return n / d
    except ZeroDivisionError:
        return 0


def get_random_from_enum(enum):
    return random.choice(list(enum))


def get_random_from_range(lst):
    return random.randrange(lst[0], lst[1])
