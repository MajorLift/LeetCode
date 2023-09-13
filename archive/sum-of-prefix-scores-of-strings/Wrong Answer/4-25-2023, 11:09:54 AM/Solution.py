// https://leetcode.com/problems/sum-of-prefix-scores-of-strings

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n = len(words)
        adj = defaultdict(set)
        for word in words:
            prefixes = [word[:k] for k in range(1, len(word) + 1)]
            for k, prefix in enumerate(prefixes):
                for p in range(k, len(prefixes)):
                    if prefixes[p] in words:
                        adj[prefix].add(prefixes[p])

        answer = []
        for word in words:
            score_sum = 0
            for prefix in [word[:k] for k in range(1, len(word) + 1)]:
                score_sum += len(adj[prefix])
            answer.append(score_sum)
        return answer
        
    def isPrefix(self, s, t):
        return len(s) <= len(t) and s == t[:len(s)]
