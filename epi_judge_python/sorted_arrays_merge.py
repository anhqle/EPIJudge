from typing import List

from test_framework import generic_test
import heapq
import collections

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:

    Element = collections.namedtuple("Element", ["value", "array", "index"])

    h = [Element(arr[0], arr_index, 0)  for (arr_index, arr) in enumerate(sorted_arrays)]
    heapq.heapify(h) 
    res = []

    while h:
        e = heapq.heappop(h)
        res.append(e.value)

        if len(sorted_arrays[e.array]) > e.index + 1:
            heapq.heappush(h, Element(sorted_arrays[e.array][e.index + 1], e.array, e.index + 1))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
