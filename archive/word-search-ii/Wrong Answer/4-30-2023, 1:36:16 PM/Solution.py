// https://leetcode.com/problems/word-search-ii

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = map(len, (board, board[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        self.root = TrieNode()
        for word in words:
            self.add(word)

        output = set()
        starts = [(board[i][j], i, j) 
            for i, j in product(range(m), range(n)) 
            if board[i][j] in self.root.children]
        for char, x, y in starts:
            stack = [(char, x, y)]
            visited = set()
            while stack:
                prefix, r, c = stack.pop()
                res = self.search(prefix)
                if res is False:
                    continue
                elif res is True:
                    pass
                else:
                    output.add(prefix)
                for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                    if not (0 <= i < m and 0 <= j < n) \
                        or (i, j) in visited:
                        continue
                    stack.append((prefix + board[i][j], i, j))
                    visited.add((i, j))
        return output

    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True
        curr.val = word

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        if curr.isEnd:
            return curr.val
        return True


class TrieNode:
    def __init__(self) -> None:
        self.children = dict()
        self.isEnd = False
        self.val = None