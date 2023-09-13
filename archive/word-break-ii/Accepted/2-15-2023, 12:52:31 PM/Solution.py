// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n, wordSet = len(s), set(wordDict)
        memo = [[] for _ in range(n + 1)]
        for r in range(1, n + 1):
            for l in range(r):
                word = s[l:r]
                if word in wordSet:
                    memo[r] += [word] if l == 0 \
                        else [partial + " " + word for partial in memo[l]]
        return memo[-1]