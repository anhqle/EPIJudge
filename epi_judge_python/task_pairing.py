import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    task_durations.sort()
    l, r = 0, len(task_durations) - 1
    res = []
    while l < r:
        res.append(PairedTasks(task_durations[l], task_durations[r]))
        l, r = l + 1, r - 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
