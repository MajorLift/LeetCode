// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [t_char for s_char, t_char in zip(*map(sorted, (s + "!", t))) if s_char != t_char].pop()