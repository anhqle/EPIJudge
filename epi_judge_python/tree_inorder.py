from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # Using recursion, O(height) space
    # if not tree:
    #     return []
    # return inorder_traversal(tree.left) + [tree.data] + inorder_traversal(tree.right)

    # Using stack, O(height) space
    # stack = []
    # cur = tree
    # res = []
    # while stack or cur:
    #     while cur:
    #         stack.append(cur)
    #         cur = cur.left
    #     cur = stack.pop()
    #     res.append(cur.data)
    #     cur = cur.right
    # return res

    # Using O(1) space, use parent field
    cur = tree
    res = []
    count_right = 0
    while cur:
        while cur.left:
            cur = cur.left
        res.append(cur)
        if cur.right:
            cur = cur.right
            count_right += 1
            continue
        if cur == cur.parent.left:
            cur = cur.parent
            cur.left = None
        else:
            for _ in range(count_right + 1):
                cur = cur.parent
            count_right = 0
            cur.left = None
    return res




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
