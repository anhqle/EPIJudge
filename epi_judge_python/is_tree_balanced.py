from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    Result = collections.namedtuple("Result", ["is_balanced", "height"])

    def check_balance(tree):
        # base case
        if not tree:
            return Result(True, 0)

        left_result = check_balance(tree.left)
        if not left_result.is_balanced:
            return Result(False, left_result.height + 1)

        right_result = check_balance(tree.right)
        if not right_result.is_balanced:
            return Result(False, right_result.height + 1)

        return Result(abs(left_result.height - right_result.height) <= 1,
                      max(left_result.height, right_result.height) + 1)

    return check_balance(tree).is_balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
