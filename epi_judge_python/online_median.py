from typing import Iterator, List
import heapq

from test_framework import generic_test
import time

def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap = []
    max_heap = []
    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        tmp = (min_heap[0] 
                    if len(min_heap) > len(max_heap) 
                    else 0.5 * (min_heap[0] + -max_heap[0]))
        result.append(tmp)
    return result
    
def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
