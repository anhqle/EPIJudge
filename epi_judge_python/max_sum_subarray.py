from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    min_so_far = total = 0
    max_so_far = 0

    for i, n in enumerate(A):
        total += n
        max_so_far = max(max_so_far, total - min_so_far)

        if total < min_so_far:
            min_so_far = total
    return max_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
