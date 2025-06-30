from typing import Optional, List, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ListNode):
            return False
        curr1, curr2 = self, other
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1 is None and curr2 is None  # Both should be exhausted

    def __repr__(self) -> str:
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return "ListNode([" + " -> ".join(vals) + "])"


class TreeNode:
    def __init__(self, val: int | None = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TreeNode):
            return False

        # Basic recursive comparison
        # For more complex scenarios (e.g. LeetCode's specific null handling in tree paths),
        # this might need to be more robust or rely on serialization.
        if self is None and other is None:
            return True
        if self is None or other is None:
            return False
        if self.val != other.val:
            return False
        return self.left == other.left and self.right == other.right

    def __repr__(self) -> str:
        # A simple representation; more complex ones (like level-order) are possible
        # This is just to give an idea. For test outputs, a serialized list form is often better.
        # For example, LeetCode often uses a list like [1,null,2,3] for tree representation.
        # Let's make a helper for a list representation for easier comparison in tests.
        return f"TreeNode(val={self.val}, left={self.left is not None}, right={self.right is not None})"
        # A better repr for testing might be a list form:
        # return str(self.to_list())

    # Helper to convert tree to list (level-order with nulls, common in LeetCode)
    # This can be used by users to define 'expected' values or by a custom comparator.
    def to_list(self) -> List[Optional[int]]:
        output: List[Optional[int]] = []
        if not self:
            return []

        queue: List[Optional[TreeNode]] = [self]

        while queue:
            node = queue.pop(0)
            if node:
                output.append(node.val)
                # Important: Add children even if they are None, up to the last non-None level
                # For perfect LeetCode compatibility, this needs to be precise about trailing nulls.
                # This is a simplified version.
                if (
                    node.left
                    or node.right
                    or any(n for n in queue if n and (n.left or n.right))
                ):  # Heuristic to add nulls
                    queue.append(node.left)
                    queue.append(node.right)
            else:
                # Only add null if there are more nodes to process at deeper levels or current level
                # This part is tricky to get exactly like LeetCode's serialization.
                # For now, we'll keep it simpler. If perfect LC serialization is needed for 'expected',
                # users might provide lists directly.
                if any(
                    n for n in queue if n
                ):  # Add null if there are more non-null nodes in queue
                    output.append(None)

        # Trim trailing Nones from the output list
        while output and output[-1] is None:
            output.pop()

        return output


# Helper functions to build these structures from lists (often how LeetCode gives input)
def list_to_linkedlist(items: List[Any]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def list_to_treenode(items: List[Optional[int]]) -> Optional[TreeNode]:
    if not items or items[0] is None:
        return None

    root = TreeNode(items[0])
    queue = [root]
    i = 1
    while i < len(items):
        current_node = queue.pop(0)

        if items[i] is not None:
            current_node.left = TreeNode(items[i])
            queue.append(current_node.left)
        i += 1

        if i < len(items) and items[i] is not None:
            current_node.right = TreeNode(items[i])
            queue.append(current_node.right)
        i += 1

    return root


def pretty_print_tree(node: Optional[TreeNode], prefix: str = "", is_left: bool = True):
    """
    Pretty prints a binary tree.

    Args:
        node: The current node to print.
        prefix: The prefix string for indentation.
        is_left: A boolean indicating if the current node is a left child.
    """
    if not node:
        return

    # Recursively print the right child first (for a more intuitive output)
    if node.right:
        pretty_print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

    # Print the current node
    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))

    # Recursively print the left child
    if node.left:
        pretty_print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


def pretty_print_linked_list(head: Optional[ListNode]):
    """
    Pretty prints a linked list.

    Args:
        head: The head of the linked list.
    """
    if not head:
        print("Empty List")
        return

    current = head
    nodes = []
    while current:
        nodes.append(str(current.val))
        current = current.next

    print(" -> ".join(nodes))
