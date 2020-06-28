from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    mat = [[None] * m] * n
    mat[-1] = [1] * m  # last row
    for i in range(n):   # last column
        mat[i][-1] = 1

    for row in reversed(range(n - 1)):
        for col in reversed(range(m - 1)):
            mat[row][col] = mat[row + 1][col] + mat[row][col + 1]

    return mat[0][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
