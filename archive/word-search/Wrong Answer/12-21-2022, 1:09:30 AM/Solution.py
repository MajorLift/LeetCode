// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)
        
        def backtrack(curr, idx):
            i, j = curr
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[idx]:
                return False
            if idx == k - 1:
                return True
            return any([backtrack(tuple(map(sum, zip(curr, offset))), idx + 1) for offset in ((-1, 0), (1, 0), (0, -1), (0, 1))])

        return m * n >= k and any([backtrack((i, j), 0) for i in range(m) for j in range(n) if board[i][j] == word[0]])