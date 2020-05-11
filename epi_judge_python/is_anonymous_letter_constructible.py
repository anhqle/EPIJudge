from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    
    d = collections.defaultdict(int)

    for c in letter_text:
        d[c] += 1
    for c in magazine_text:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
            if not d:
                return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
