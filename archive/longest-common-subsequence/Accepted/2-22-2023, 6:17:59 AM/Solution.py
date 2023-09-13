// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        shorter, longer = sorted([text1, text2], key=len)
        n1, n2 = len(shorter), len(longer)
        prev, curr = [0] * (n1 + 1), [0] * (n1 + 1)
        for i in range(n2 - 1 , -1, -1):
            for j in range(n1 - 1, -1, -1):
                curr[j] = 1 + prev[j + 1] if shorter[j] == longer[i] \
                    else max(prev[j], curr[j + 1])
            prev, curr = curr, prev
        return prev[0]