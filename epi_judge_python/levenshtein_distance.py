from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    cache = [[-1] * len(B) for _ in range(len(A))]
    cache[0][0] = 0 if A[0] == B[0] else 1

    def util(a, b, cache = cache):
        if a < 0:
            return 1 + b
        if b < 0:
            return 1 + a

        # Return if result is already cached
        if cache[a][b] != -1:
            return cache[a][b]

        if A[a] == B[b]:
            cache[a][b] = util(a - 1, b - 1)
        else:
            cache[a][b] = 1 + min(util(a - 1, b - 1), util(a, b - 1), util(a - 1, b))

        return cache[a][b]

    return util(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
