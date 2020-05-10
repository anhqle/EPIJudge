from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    
    L, U = 0, len(A) - 1
    result = []
    while L <= U:
        mid = (L + U) // 2
        if A[mid] == k:
            result.append(mid)
            U = mid - 1
        elif A[mid] < k:
            L = mid + 1
        elif A[mid] > k:
            U = mid - 1
            
    return min(result) if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
