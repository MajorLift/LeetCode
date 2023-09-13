// https://leetcode.com/problems/alien-dictionary

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        all_chars = set(char for word in words for char in word)
        if len(words) < 2:
            return "".join(all_chars)
        adj, indegrees = {k: set() for k in all_chars}, {k: 0 for k in all_chars}

        for l, r in zip(words, words[1:]):
            for u, v in zip(l, r):
                if u != v:
                    if v not in adj[u]:
                        adj[u].add(v)
                        indegrees[v] += 1
                    break
            else:
                if len(l) > len(r):
                    return ""
        
        cycle = defaultdict(bool)
        output = []
        def dfs(char):
            if char in cycle:
                return cycle[char]
            cycle[char] = False
            for node in adj[char]:
                if not dfs(node):
                    return False
            cycle[char] = True
            output.append(char)
            return True
        return "".join(output[::-1]) \
            if all(dfs(node) for node, indegree in indegrees.items() if indegree == 0) \
            else ""
