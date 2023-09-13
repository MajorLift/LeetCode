// https://leetcode.com/problems/word-ladder-ii

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words, output = set(wordList + [beginWord]), []
        if endWord not in words:
            return []
        queue = deque([(endWord, [endWord])])
        while queue:
            next_queue = deque()
            while queue:
                word, path = queue.popleft()
                if word == beginWord:
                    output.append(path[::-1])
                visited = set(path)
                for i in range(len(word)):
                    for k in range(26):
                        s = word[:i] + chr(ord("a") + k) + word[i+1:]
                        if s not in visited and s in words:
                            next_queue.append((s, path + [s]))
            if output:
                break
            queue = next_queue
        return output