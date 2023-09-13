// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        curr = root
        if not curr:
            return 0
        height = 1
        leftwise = 0
        # find last node
        while curr.left or curr.right:
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
                leftwise += 1
            height += 1
        return (1 << height) - 1 - leftwise