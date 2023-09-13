// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)

        word_chars, board_chars = set([*word]), set([e for row in board for e in row])
        if m * n < k or not board_chars.issuperset(word_chars):
            return False

        def backtrack(coord, idx):
            x, y = coord
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != word[idx]:
                return False
            if idx == k - 1:
                return True

            board[x][y] = "0"
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if backtrack((i, j), idx + 1):
                    return True
            return False

        board_default = copy.deepcopy(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack((i, j), 0): 
                        return True
                    board = board_default
        return False