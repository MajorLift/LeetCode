// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return root.val > root.left.val and self.isValidBST(root.left) if root.left and root.val < root.right.val and self.isValidBST(root.right) if root.right