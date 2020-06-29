import collections
import functools
from typing import List
from collections import deque
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:

    mat = []
    for row in range(len(items)):
        mat.append([None] * (capacity + 1))
    
    # first row
    for w in range(capacity + 1):
        mat[0][w] = items[0].value if items[0].weight <= w else 0
        
    for row in range(1, len(items)):
        candidate = items[row]
        c_w = candidate.weight
        c_v = candidate.value
        for w in range(capacity + 1):
            if candidate.weight > w:
                mat[row][w] = mat[row - 1][w]
            else:
                v = max(mat[row - 1][w - c_w] + c_v, mat[row - 1][w])
                mat[row][w] = v
    
    return mat[-1][-1]



@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
