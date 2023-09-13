// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.root = root
        sPath, dPath = self.getPath(root, startValue), self.getPath(root, destValue)
        lca = self.getLCA(sPath, dPath)
        sPath, dPath = sPath[lca:], dPath[lca:]
        return ''.join(['U'] * len(sPath) + dPath)

    def getPath(self, curr, target, path=[]):
        if not curr:
            return False
        if curr.val == target:
            return path
        return self.getPath(curr.left, target, path + ['L']) \
            or self.getPath(curr.right, target, path + ['R'])

    def getLCA(self, aPath, bPath):
        for i, (a, b) in enumerate(zip(aPath, bPath)):
            if a != b:
                return max(i - 1, 0)
        return 0
            
        