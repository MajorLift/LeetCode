// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7

        sums = []
        def sum_tree(node):
            if not node:
                return 0
            curr = node.val + sum_tree(node.left) + sum_tree(node.right)
            sums.append(curr)
            return curr

        total = sum_tree(root)
        ans = 0
        for e in sums:
            ans = max(ans, e * (total - e))
        return ans % MOD
