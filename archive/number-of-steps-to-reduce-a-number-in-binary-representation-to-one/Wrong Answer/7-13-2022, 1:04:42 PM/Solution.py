// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one

class Solution:
    def numSteps(self, s: str) -> int:
        curr = s[:]
        steps = 0
        for i in range(len(s)):
            if curr[-1] == "1":
                steps += 1
            curr = curr[:-1]
            if len(curr) > 0:
                steps += 1
        return steps