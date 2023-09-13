// https://leetcode.com/problems/word-ladder-ii

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words, output = set(wordList + [beginWord]), []
        if endWord not in words:
            return []
        adj = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)
        dist = defaultdict(lambda: +math.inf)
        dist[endWord] = 0
        level = 0

        queue = deque([(endWord, [endWord])])
        while queue:
            level += 1
            next_queue = deque()
            while queue:
                word, path = queue.popleft()
                if word == beginWord:
                    output.append(path[::-1])
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    if pattern not in adj:
                        continue
                    for neighbor in adj[pattern]:
                        if level + 1 <= dist[neighbor]:
                            dist[neighbor] = level + 1
                            next_queue.append((neighbor, path + [neighbor]))
            queue = next_queue
        return output