from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    w, pA, pB = -1, m - 1, n - 1
    while pA >= 0 and pB >= 0:
        if A[pA] > B[pB]:
            A[w] = A[pA]
            pA -= 1
        else:
            A[w] = B[pB]
            pB -= 1
        w -= 1
    if pB >= 0:
        A[:pB + 1] = B[:pB + 1]

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
