// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def recurse(node, maxInPath):
            nonlocal count
            newMax = max(maxInPath, node.val)
            if newMax == maxInPath:
                count += 1
            if node.left:
                recurse(node.left, newMax)
            if node.right:
                recurse(node.right, newMax)
        recurse(root, root.val)
        return count
        