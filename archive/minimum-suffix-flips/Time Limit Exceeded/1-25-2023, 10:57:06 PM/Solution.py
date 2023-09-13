// https://leetcode.com/problems/minimum-suffix-flips

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        s = ["0"] * n
        ans = 0
        for i in range(n):
            if s[i] != target[i]:
                for j in range(i, n):
                    s[j] = "1" if s[j] == "0" else "0"
                ans += 1
        return ans