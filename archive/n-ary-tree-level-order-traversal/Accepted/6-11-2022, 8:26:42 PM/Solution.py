// https://leetcode.com/problems/n-ary-tree-level-order-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        output = [[root.val]]
        queue = deque([(root, 0)])
        prev_height = -1
        while queue:
            curr, curr_height = queue.popleft()
            if curr_height > prev_height:
                output.append([])
            
            for node in curr.children:
                if node:
                    queue.append((node, curr_height + 1)) 
                    output[curr_height + 1].append(node.val)
                    
        return list(filter(lambda x: len(x) > 0, output))