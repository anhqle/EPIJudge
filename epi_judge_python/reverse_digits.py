from test_framework import generic_test


def reverse(x: int) -> int:
    res = []
    negative_sign = x < 0
    while x != 0:
        res.append(str(x % 10))
        x = x // 10
    return int(''.join(res)) * (-1 if negative_sign else 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
