// https://leetcode.com/problems/search-suggestions-system

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.add_word(product)
        
        output, curr = [], trie.root
        for char in searchWord:
            curr = curr.get_child(char)
            output.append(sorted(curr.get_descendants())[:3])
        return output
            
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return str([e for e in self.root.children if e])

    def add_word(self, word):
        curr = self.root
        for i, char in enumerate(word):
            if not curr: break
            curr = curr.add_child(char, i == len(word) - 1)

    @staticmethod
    def char_idx(char):
        return ord(char) - ord('a')

class TrieNode:
    def __init__(self, val=None, prefix='', isEnd=None, children=None):
        self.val = val
        self.prefix = prefix
        self.isEnd = isEnd or False
        self.children = children or [None] * 26

    def __repr__(self):
        return f'val: {self.val}, prefix: {self.prefix}, isEnd: {self.isEnd}, children: {str([e for e in self.children if e])}'

    def get_child(self, val):
        return self.children[Trie.char_idx(val)]

    def has_child(self, val):
        return self.children[Trie.char_idx(val)] is not None

    def add_child(self, val, isEnd):
        if not self.has_child(val):
            self.children[Trie.char_idx(val)] = TrieNode(val, self.prefix + val, isEnd)
        return self.get_child(val)

    def get_descendants(self):
        output, stack = [], [self]
        while stack:
            curr = stack.pop()
            if curr.isEnd:
                output.append(curr.prefix)
            for child in curr.children:
                if not child: continue
                stack.append(child)
        return output
