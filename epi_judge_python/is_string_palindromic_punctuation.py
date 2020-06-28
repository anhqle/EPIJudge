from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    l, r = 0, len(s) - 1
    while l <= r:
        while 0 <= l < len(s) and not s[l].isalnum():
            l += 1
        while 0 <= r < len(s) and not s[r].isalnum():
            r -= 1
        if l <= r and s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
