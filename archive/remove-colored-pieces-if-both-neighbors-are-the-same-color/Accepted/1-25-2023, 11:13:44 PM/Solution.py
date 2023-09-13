// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def total_score(player):
            return sum(max(len(seg) - 2, 0) \
                for seg in colors.split("A" if player == "B" else "B") \
                if seg)
        return total_score("A") > total_score("B")