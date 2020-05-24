from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:

    def print_outside(m) -> List[int]:
        res = []
        k = len(m) # dimension

        res += m[0] # add first row
        for i in range(1, k):
            # add last column
            res.append(m[i][k - 1])
        for j in reversed(range(k - 1)):
            # add last row
            res.append(m[k-1][j])
        for i in reversed(range(1, k - 1)):
            # add first column
            res.append(m[i][0])
        return res

    if not square_matrix:
        return []
    
    res = []    
    res += print_outside(square_matrix)
    k = len(square_matrix)
    inside_matrix = [row[1:k-1] for row in square_matrix[1:k - 1]]
    res += matrix_in_spiral_order(inside_matrix)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
