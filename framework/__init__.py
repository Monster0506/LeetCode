from .framework import run_leetcode_tests, TimeoutError

from .datastructures import (
    ListNode,
    TreeNode,
    list_to_linkedlist,
    list_to_treenode,
    pretty_print_tree,
    pretty_print_linked_list,
)


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"


__all__ = [
    "run_leetcode_tests",
    "TimeoutError",
    "ListNode",
    "TreeNode",
    "list_to_linkedlist",
    "list_to_treenode",
    "Colors",
    "pretty_print_linked_list",
    "pretty_print_tree",
]
