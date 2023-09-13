// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)
        
        def backtrack(path, curr, idx):
            if idx == k - 1:
                return True
            x, y = curr
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < m and 0 <= j < n \
                    and (i, j) not in path \
                    and board[i][j] == word[idx + 1]:
                    path.add((i, j))
                    if backtrack(path, (i, j), idx + 1):
                        return True
                    path.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(set((i, j)), (i, j), 0):
                        return True
        return False