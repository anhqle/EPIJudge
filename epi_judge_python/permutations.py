from typing import List
from next_permutation import next_permutation
from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:

    # res = []
    # def backtrack(l, options):
    #     if len(l) == len(A):
    #         res.append(l.copy())
    #         return
        
    #     for i, v in enumerate(options):
    #         l.append(v)
    #         new_options = options.copy()
    #         new_options.pop(i)
    #         backtrack(l, new_options)
    #         l.pop()

    # backtrack([], A)
    # return res

    ## From book: A variant that does almost the same thing except
    ##   making use of the array to hold the options (instead of using new array to hold options)
    res = []
    def directed_permutations(i):
        # Generate permutation from i onwards
        if i == len(A) - 1:
            res.append(A.copy())
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]  # make move
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]  # unmake move
    directed_permutations(0)
    return res

    ## Using next_permutation
    # res = []
    # perm = sorted(A)
    # while perm:
    #     res.append(perm)
    #     perm = next_permutation(perm)
    # return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
