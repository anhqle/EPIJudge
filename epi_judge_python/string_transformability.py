from typing import Set
from collections import deque
from test_framework import generic_test
import string

def transform_string(D: Set[str], s: str, t: str) -> int:

    def mutate_string(s):
        for i in range(len(s)):
            for c in string.ascii_lowercase:
                yield s[:i] + c + s[i + 1:]

    myqueue = deque([(s, 0)])

    while myqueue:
        cur, path = myqueue.popleft()
        if cur == t:
            return path
        for candidate in mutate_string(cur):
            if candidate in D:
                myqueue.append((candidate, path + 1))
                D.remove(candidate)

    return -1  # not found

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
