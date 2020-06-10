from typing import List
import random
from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:

    def partition(A) -> int:
        "Return the index of the pivot"
        #pivot_index = random.randint(0, len(A) - 1)
        pivot_index = -1
        pivot = A[pivot_index]
        A[-1], A[pivot_index] = A[pivot_index], A[-1]
        small = 0
        for i in range(len(A) - 1):
            if A[i] <= pivot:
                A[i], A[small] = A[small], A[i]
                small += 1
        A[-1], A[small] = A[small], A[-1] # put the pivot in place
        return small

    if len(A) == 1 and k == 1:
        return A[0]

    random.shuffle(A)
    pivot_index = partition(A)
    if k == len(A) - pivot_index:
        return A[pivot_index]
    elif k > len(A) - pivot_index:
        return find_kth_largest(k - (len(A) - pivot_index), A[:pivot_index])
    else:
        return find_kth_largest(k, A[pivot_index + 1:])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
