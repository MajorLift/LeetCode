class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def total_score(player):
            return sum(max(len(seg) - 2, 0) \
                for seg in colors.split(("A", "B")[player == "A"]) \
                if seg)
        return total_score("A") > total_score("B")