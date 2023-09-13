// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        return sum([max(len(seg) - 2, 0) for seg in colors.split("B") if seg]) > sum([max(len(seg) - 2, 0) for seg in colors.split("A") if seg])