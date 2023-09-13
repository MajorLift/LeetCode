// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one

class Solution:
    def numSteps(self, s: str) -> int:
        steps = len(s) - 1
        steps += len([char for char in s if char == '1'])
        return steps