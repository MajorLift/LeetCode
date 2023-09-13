// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        self.visited[node] = clone = Node(node.val, [])
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(v) for v in node.neighbors]
        return clone