// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        m = len(queries)
        self.state = defaultdict(lambda: [0, 0, [1]])    # depth, height, path
        self.state[1] = [0, 0, [1]]
        self.dfs(root)
        # print(self.state)
        answer = []
        for query in queries:
            temp = {**self.state}
            _, height, path = temp[query]
            for node in path:
                temp[node][1] -= height + 1
            answer.append(sorted(temp.items(), key=lambda x: x[1][0] + x[1][1], reverse=True)[0][0])
        return answer
        
    def dfs(self, node):
        if not node or (not node.left and not node.right):
            return 0
        depth, height, path = self.state[node.val]
        if node.left:
            self.state[node.left.val] = [depth + 1, self.dfs(node.left), path + [node.left.val]]
        if node.right:
            self.state[node.right.val] = [depth + 1, self.dfs(node.right), path + [node.right.val]]
        new_height = 1 + max(self.dfs(node.left), self.dfs(node.right))
        self.state[node.val][1] = new_height
        return new_height