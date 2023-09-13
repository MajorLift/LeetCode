// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moves_a, moves_b = [max(len(seg) - 2, 0) for seg in colors.split("B")], [max(len(seg) - 2, 0) for seg in colors.split("A")]
        return sum(moves_a) > sum(moves_b)