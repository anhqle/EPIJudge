from typing import Iterator
from collections import Counter
from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    c = Counter(stream)
    max_k = ''
    max_v = 0
    for k, v in c.items():
        if v > max_v:
            max_k = k
            max_v = v
    return max_k


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
