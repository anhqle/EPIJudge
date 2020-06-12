from typing import List
from copy import copy

from test_framework import generic_test
from copy import copy

def n_queens(n: int) -> List[List[int]]:
    col_placement = [None] * n    
    res = []
    def n_queens_solve(row):
        if row == n:
            res.append(copy(col_placement))
            return
        for col in range(n):
            if (col not in col_placement[:row]  # not in same the col as previous
                and all([abs(r - row) != abs(col - c) for r, c in enumerate(col_placement[:row])])):
                col_placement[row] = col
                n_queens_solve(row + 1)

    n_queens_solve(0)
    return res




def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
