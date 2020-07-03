from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    
    dummy_odd, dummy_even = ListNode(None), ListNode(None)
    tails = [dummy_even, dummy_odd]
    turn = 0
    while L:
        tails[turn].next = L
        tails[turn] = tails[turn].next
        L = L.next
        turn = (turn + 1) % 2

    tails[0].next = dummy_odd.next
    tails[1].next = None

    return dummy_even.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
