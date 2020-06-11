from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:

    def is_bst(tree, lo, hi) -> bool:
        if not tree:
            return True
        return (lo <= tree.data <= hi
            and is_bst(tree.left, lo, tree.data)
            and is_bst(tree.right, tree.data, hi))

    return is_bst(tree, float('-inf'), float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
