// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n, k = map(len, (board, board[0], word))
        EMPTY, BLOCKED = ' ', '#'
        for row in board + list(zip(*board)):
            for s in ''.join(row).split('#'):
                for w in (word, word[::-1]):
                    if len(s) == k and all(s[i] == w[i] or s[i] == EMPTY for i in range(k)):
                        return True
        return False