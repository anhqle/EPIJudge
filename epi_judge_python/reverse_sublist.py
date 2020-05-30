from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    n1 = ListNode(None, next = L)
    for _ in range(start - 1):
        n1 = n1.next
    n2 = n1.next

    counter = 0
    while (counter < finish - start) and n2.next:
        iter = n2.next # the node we'll operate on
        n2.next = iter.next # save its next before we operate on it
        iter.next = n1.next # revert it
        n1.next = iter
        counter += 1

    if start > 1:
        return L
    else:
        return n1.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
