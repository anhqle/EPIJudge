from test_framework import generic_test


def square_root(k: int) -> int:

    if k == 0:
        return 0

    candidates = range(k + 1)
    l, r = 0, len(candidates) - 1

    while l <= r:
        i = (l + r) // 2
        square = candidates[i] * candidates[i]
        if square == k:
            return candidates[i]
        elif square < k:
            l = i + 1
        elif square > k:
            r = i - 1

    if square > k:
        return candidates[i - 1]
    elif square < k:
        return candidates[i]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
