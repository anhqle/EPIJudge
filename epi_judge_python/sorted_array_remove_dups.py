import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if len(A) <= 1:
        return len(A)
    w, r = 0, 0
    while r < len(A):
        while r < len(A) and A[r] == A[w]:
            r += 1
        if r < len(A):
            A[w + 1] = A[r]
            w += 1
    return w + 1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
