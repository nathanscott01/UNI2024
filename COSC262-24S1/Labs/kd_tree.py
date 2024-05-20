"""
Nathan Scott
COSC262 Lab 11
KD Trees
"""

# Do not alter the next two lines
from collections import namedtuple

Node = namedtuple("Node", ["value", "left", "right"])


# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False, left=0, right=0):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
        right = len(nums)
    if right - left == 1:
        tree = Node(nums[left], None, None)  # A leaf
    else:
        mid = (left + right) // 2
        left_tree = binary_search_tree(nums, True, left, mid)
        right_tree = binary_search_tree(nums, True, mid, right)
        tree = Node(nums[mid - 1], left_tree, right_tree)
    return tree


# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None:  # Leaf?
        return 2 * level * ' ' + f"Leaf({tree.value})\n"
    else:
        result = 2 * level * ' ' + f"Node({tree.value})\n"
        result += print_tree(tree.left, level + 1)
        result += print_tree(tree.right, level + 1)
        return result
