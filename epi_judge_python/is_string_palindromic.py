from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    l,  r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1

    return True

# def is_palindromic(s: str) -> bool:
#     if len(s) <= 1:
#         return True

#     return s[0] == s[-1] and is_palindromic(s[1:-1])



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
