from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:

    def merge_sort(s):
        if not s or not s.next:
            return s
        dummy = ListNode(None, next = s)
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        s2 = merge_sort(slow.next) # Sort second half first
        # Sort first half
        slow.next = None
        s1 = merge_sort(s) 
        

        d = ListNode(None)
        cur, p1, p2 = d, s1, s2
        while p1 and p2:
            if p1.data <= p2.data:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2
        return d.next

    return merge_sort(L)


    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
