from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    result = []
    a = b = 0
    last_added = None

    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            if A[a] != last_added:
                result.append(A[a])
                last_added = A[a]
            a += 1
            b += 1
        elif A[a] < B[b]:
            a += 1
        elif A[a] > B[b]:
            b += 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
