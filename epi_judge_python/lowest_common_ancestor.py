import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    Result = namedtuple("Result", ['ancestor', 'n'])
    def lca_helper(tree, node0, node1):
        if not tree: # base case
            return Result(None, 0)

        # return tree if one node is in left and the other in right
        l = lca_helper(tree.left, node0, node1)
        r = lca_helper(tree.right, node0, node1) 

        if l.ancestor or r.ancestor:
            return Result(l.ancestor or r.ancestor, l.n + r.n)
        
        total = l.n + r.n + (1 if tree == node0 else 0) + (1 if tree == node1 else 0) 

        return Result(tree if total == 2 else None, total)

    return lca_helper(tree, node0, node1).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
