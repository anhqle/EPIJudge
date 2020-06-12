from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    def has_two_sum(A, t):
        # Assume A is sorted
        l, r = 0, len(A) - 1
        while l <= r:
            tmp = A[l] + A[r]
            if tmp == t:
                return True
            elif tmp > t:
                r -= 1
            elif tmp < t:
                l += 1
        return False

    A.sort()
    for a in A:
        if has_two_sum(A, t - a):
            return True
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
