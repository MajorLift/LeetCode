// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        m, n = len(board), len(board[0])
        k = len(word)
        if m * n <= k:
            return False
        
        def backtrack(curr, idx):
            if idx == k - 1:
                return True
            x, y = curr
            char = board[x][y]
            board[x][y] = "#"
            for offset in DIRS:
                i, j = tuple(map(sum, zip(curr, offset)))
                if not (0 <= i < m and 0 <= j < n) or board[i][j] == "#":
                    continue
                if board[i][j] == word[idx + 1] and backtrack((i, j), idx + 1):
                    return True
            board[x][y] = char
            return False

        return any([backtrack((i, j), 0) for i in range(m) for j in range(n) if board[i][j] == word[0]])