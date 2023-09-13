// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n, wordSet = len(s), set(wordDict)
        memo = [[] for _ in range(n + 1)]
        for r in range(1, n + 1):
            for l in range(r + 1):
                if s[l:r] in wordSet:
                    if l == 0:
                        memo[r].append(s[l:r])
                    else:
                        memo[r].extend([" ".join([fragment, s[l:r]]) for fragment in memo[l]])
        return memo[-1]