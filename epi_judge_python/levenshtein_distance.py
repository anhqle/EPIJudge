from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    cache = {}
    def util(A, B):
        if len(A) == 0 or len(B) == 0:
            cache[(A, B)] = len(A) or len(B)
            return cache[(A, B)]

        if A[-1] == B[-1]:
            cache[(A, B)] = cache.get((A[:-1], B[:-1]), None) or util(A[:-1], B[:-1])
        else:
            sub = cache.get((A[:-1], B[:-1]), None) or util(A[:-1], B[:-1])
            delete = cache.get((A[:-1], B), None) or util(A[:-1], B)
            add = cache.get((A, B[:-1]), None) or util(A, B[:-1])
            cache[(A, B)] = 1 + min(sub, delete, add)
        return cache[(A, B)]

    return util(A, B)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
