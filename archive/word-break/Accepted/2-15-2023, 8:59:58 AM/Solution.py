// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, wordSet = len(s), set(wordDict)
        memo = [True] + [False] * n
        for r in range(1, n + 1):
            for l in range(r):
                if memo[l] and s[l:r] in wordSet:
                    memo[r] = True
                    break
        return memo[-1]