// https://leetcode.com/problems/word-ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words, visited = set(wordList), set()
        queue = collections.deque([beginWord])
        dist = 0
        word = ''
        while queue:
            dist += 1
            next_queue = deque([])
            while queue:
                word = queue.popleft()
                for i in range(len(word)):
                    for k in range(26):
                        s = word[:i] + chr(ord("a") + k) + word[i+1:]
                        if s in words and s not in visited:
                            visited.add(s)
                            next_queue.append(s)
            queue = next_queue
        return dist if word == endWord else 0