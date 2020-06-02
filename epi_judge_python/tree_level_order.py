from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []

    qn = deque([1])
    qv = deque([tree])
    res = []
    while qn:
        res_lvl = []
        count = 0
        num = qn.popleft()
        for _ in range(num):
            node = qv.popleft()
            res_lvl.append(node.data)
            if node.left:
                count += 1
                qv.append(node.left)
            if node.right:
                count += 1
                qv.append(node.right)
        if count > 0:
            qn.append(count)
        res.append(res_lvl)

    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
