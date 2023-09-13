// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)        
        @cache
        def dp(start):
            if start == n:
                return True
            for end in range(start + 1, n + 1):
                if s[start:end] in wordSet and dp(end):
                    return True
            return False
        return dp(0)