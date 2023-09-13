// https://leetcode.com/problems/delete-nodes-and-return-forest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        output = []

        def dfs(curr):
            if not curr: return None            
            curr.left, curr.right = map(dfs, (curr.left, curr.right))
            if curr.val in to_delete:
                if curr.left: output.append(curr.left)
                if curr.right: output.append(curr.right)
                return None
            return curr
            
        root = dfs(root)
        if root: output.append(root)
        return output