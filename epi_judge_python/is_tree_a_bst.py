from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:

    def is_bst(tree: BinaryTreeNode) -> (bool, int, int):
        # return BST status, min, max
        if tree is None:
            return True, math.inf, -math.inf

        left_bst, left_min, left_max = is_bst(tree.left)
        right_bst, right_min, right_max = is_bst(tree.right)
        
        return (left_bst and right_bst and left_max <= tree.data and right_min >= tree.data,
            min(left_min, tree.data), max(right_max, tree.data)
        )

    return is_bst(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
