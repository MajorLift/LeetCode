// https://leetcode.com/problems/word-ladder-ii

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words, output = set(wordList), []
        min_dist = +math.inf
        pq = [(0, beginWord, [beginWord])]
        while pq:
            dist, word, path = heapq.heappop(pq)
            visited = set(path)
            if word == endWord:
                if dist < min_dist:
                    min_dist = dist
                    output = [path]
                elif dist == min_dist:
                    output.append(path)
            for i in range(len(word)):
                for k in range(26):
                    s = word[:i] + chr(ord("a") + k) + word[i+1:]
                    if s not in visited and s in words:
                        heapq.heappush(pq, (dist + 1, s, path + [s]))
        return output