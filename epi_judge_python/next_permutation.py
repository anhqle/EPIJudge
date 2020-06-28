from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:

    if len(perm) <= 1:
        return []

    i = len(perm) - 2
    while i >= 0:
        if perm[i] >= perm[i+1]:
            i -= 1
        else:
            for j in reversed(range(len(perm))):
                if perm[i] < perm[j]:
                    perm[i], perm[j] = perm[j], perm[i]
                    return perm[:i+1] + sorted(perm[i+1:])

    return []

    # i = len(perm) - 2
    # while i >= 0 and perm[i] >= perm[i + 1]:
    #     i -= 1

    # if i < 0:
    #     return []

    # print(i, len(perm))
    # for j in reversed(range(len(perm))):
    #     if perm[i] < perm[j]:
    #         perm[i], perm[j] = perm[j], perm[i]
    #         return perm[:i + 1] + sorted(perm[i + 1:])




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
