// https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        if not root:
            return
        stack = [root]
        while stack:
            curr = stack.pop()
            output.append(curr.val)
            for node in curr.children:
                if node:
                    stack.append(node)
        return output[::-1]