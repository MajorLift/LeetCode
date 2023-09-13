// https://leetcode.com/problems/implement-trie-prefix-tree

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.children[self.getOrd(char)]:
                curr.children[self.getOrd(char)] = TrieNode(val=char)
            curr = curr.children[self.getOrd(char)]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not curr.children[self.getOrd(char)]:
                return False
            curr = curr.children[self.getOrd(char)]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not curr.children[self.getOrd(char)]:
                return False
            curr = curr.children[self.getOrd(char)]
        return True

    def getOrd(self, char):
        return ord(char) - ord('a')

class TrieNode:
    def __init__(self, val=None, children=[None] * 26, isEnd=False):
        self.val = val
        self.children = children
        self.isEnd = isEnd

    def __repr__(self):
        return f'val: {self.val}, children: {self.children}, isEnd: {self.isEnd}'


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)