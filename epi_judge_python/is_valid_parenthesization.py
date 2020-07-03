from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    stack = []
    for c in s:
        if c in brackets.keys():
            stack.append(c)
        else:
            if not stack or c != brackets[stack.pop()]:
                return False

    return len(stack) == 0

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
