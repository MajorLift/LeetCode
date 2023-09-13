// https://leetcode.com/problems/delete-nodes-and-return-forest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = [root]
        output = [root]
        for target in to_delete:
            next_roots = []
            for start in roots:
                next_roots.extend(self.find(root, target))
            roots = next_roots
            output.extend(next_roots)
        return output
        
    def find(self, curr, target)-> List[TreeNode]:
        output = []
        if curr.left:
            output.extend(self.find(curr.left, target))
            if curr.val == target:
                output.append(curr.left)
                curr.left = None
        if curr.right:
            output.extend(self.find(curr.right, target))
            if curr.val == target:
                output.append(curr.right)
                curr.right = None
        if curr.val == target:
            curr.val = 'null'
        return output