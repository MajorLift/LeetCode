// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lo, hi):
            return lo < node.val < hi \
                and (not node.left or validate(node.left, lo, node.val)) \
                and (not node.right or validate(node.right, node.val, hi))
        return validate(root, -math.inf, +math.inf)