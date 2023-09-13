// https://leetcode.com/problems/alien-dictionary

from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        output = []
        adj = defaultdict(set)
        indegree = [-1] * 26
        for word in words:
            for char in word:
                indegree[ord(char) - ord("a")] = max(0, indegree[ord(char) - ord("a")])

        for left, right in zip(words, words[1:]):
            for u, v in zip(left, right):
                if u != v:
                    if v not in adj[u]:
                        adj[u].add(v)
                        indegree[ord(v) - ord("a")] += 1
                    break
            else:
                if len(left) > len(right):
                    return ""
                if len(left) == len(right) == 1 and left[0] not in output:
                    output.append(left[0])
        
        queue = deque([char for char in adj.keys() if indegree[ord(char) - ord("a")] == 0])
        while queue:
            curr = queue.popleft()
            output.append(curr)
            for char in adj[curr]:
                indegree[ord(char) - ord("a")] -= 1
                if indegree[ord(char) - ord("a")] == 0:
                    queue.append(char)
        
        return "".join(output) if len(output) == len([x for x in indegree if x >= 0]) else ""