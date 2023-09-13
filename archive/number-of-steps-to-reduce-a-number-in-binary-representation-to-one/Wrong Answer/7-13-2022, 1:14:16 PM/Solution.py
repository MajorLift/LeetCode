// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one

class Solution:
    def numSteps(self, s: str) -> int:
        curr = list(s)[::-1]
        steps = 0
        for i,e in enumerate(curr):
            if e == '1':
                steps += 1
            if i < len(curr) - 1:
                steps += 1
        return steps