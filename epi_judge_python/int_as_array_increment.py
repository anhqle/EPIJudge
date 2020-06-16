from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(len(A) - 1)):
        A[i] += (A[i + 1] // 10)
        A[i + 1] %= 10 
    if A[0] == 10:
        A[0] = 0
        return [1] + A
    else:
        return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
