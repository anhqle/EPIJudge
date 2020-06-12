from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    res = []
    # base case
    def find_k(tree, k, res):
        if len(res) == k:
            return None
        if not tree:
            return None
        find_k(tree.right, k, res)
        if len(res) < k:
            res.append(tree.data)
        find_k(tree.left, k, res)

    find_k(tree, k, res)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
