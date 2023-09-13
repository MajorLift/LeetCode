// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n, k = map(len, (board, board[0], word))
        EMPTY, BLOCKED = ' ', '#'
        row_cnt = col_cnt = 0
        row_acc, col_acc = [], []
        for i in range(m):
            if row_cnt == k:
                p = 0
                while p < k:
                    if row_acc[p] != EMPTY and row_acc[p] != word[p]:
                        break
                    p += 1
                if p == k:
                    return True
            if col_cnt == k:
                p = 0
                while p < k:
                    if col_acc[p] != EMPTY and col_acc[p] != word[p]:
                        break
                    p += 1
                if p == k:
                    return True
            row_cnt = col_cnt = 0
            row_acc, col_acc = [], []
            for j in range(n):
                if board[i][j] == BLOCKED:
                    if row_cnt == k:
                        p = 0
                        while p < k:
                            if row_acc[p] != EMPTY and row_acc[p] != word[p]:
                                break
                            p += 1
                        if p == k:
                            return True
                    row_cnt = 0
                    row_acc = []
                else:
                    row_acc.append(board[i][j])
                    row_cnt += 1
                if board[j][i] == BLOCKED:
                    if col_cnt == k:
                        p = 0
                        while p < k:
                            if col_acc[p] != EMPTY and col_acc[p] != word[p]:
                                break
                            p += 1
                        if p == k:
                            return True
                    col_cnt = 0
                    col_acc = []
                else:
                    col_acc.append(board[j][i])
                    col_cnt += 1
        return False