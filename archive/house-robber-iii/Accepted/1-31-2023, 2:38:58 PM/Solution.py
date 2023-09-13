// https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            subchilds = []
            if node.left:
                subchilds += [node.left.left, node.left.right]
            if node.right:
                subchilds += [node.right.left, node.right.right]
            return max(node.val + sum([dp(v) for v in subchilds]), sum([dp(node.left), dp(node.right)]))
        return dp(root)