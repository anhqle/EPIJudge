from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
import time


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # Track where we came from
    prev, result = None, []
    while tree: # while there's still a node to print
        if prev == tree.parent:
            # Coming down from top
            if tree.left:
                next = tree.left
            else:
                result.append(tree.data)
                next = tree.right or tree.parent
        elif prev == tree.left:
            # Coming up from left
            result.append(tree.data)
            next = tree.right or tree.parent
        elif prev == tree.right:
            next = tree.parent

        prev, tree = tree, next  # end condition is when next is parent of root, and thus None
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
