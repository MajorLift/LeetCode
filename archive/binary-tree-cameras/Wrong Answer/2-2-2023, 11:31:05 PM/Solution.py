// https://leetcode.com/problems/binary-tree-cameras

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node):
            if not node:
                return 0
            subchilds = []
            if node.left:
                subchilds += [node.left.left, node.left.right]
            if node.right:
                subchilds += [node.right.left, node.right.right]
            return 1 + sum([dp(v) for v in subchilds])
        return min(dp(root), sum([dp(root.left), dp(root.right)]))