// https://leetcode.com/problems/maximum-score-of-a-node-sequence

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        def score(seq):
            for i in range(3):
                if seq[i + 1] not in adj[seq[i]]:
                    return -1
            return sum([scores[i] for i in seq])

        seqs = permutations(range(n), 4)
        return max([score(seq) for seq in seqs])