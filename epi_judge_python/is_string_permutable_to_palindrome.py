from test_framework import generic_test
import collections

def can_form_palindrome(s: str) -> bool:
    d = collections.defaultdict(int)
    for c in s:
        d[c] += 1

    odd_count = 0
    for v in d.values():
        if v % 2 != 0:
            odd_count += 1

    return odd_count <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
