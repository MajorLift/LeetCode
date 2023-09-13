// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        self.inorderTraversal(root.left)
        if root.val is None: 
            return
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result
        