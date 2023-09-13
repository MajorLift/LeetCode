// https://leetcode.com/problems/word-ladder-ii

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        output = []
        words = set(wordList + [beginWord])
        if endWord not in words:
            return []

        adj = defaultdict(list)
        for word in set(words):
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)

        tree = defaultdict(set)
        dist = defaultdict(lambda: +math.inf)
        dist[endWord] = 0
        level = 0
        queue = deque([[endWord]])
        while queue:
            level += 1
            next_queue = deque()
            while queue:
                path = queue.popleft()
                word = path[-1]
                if word == beginWord:
                    output.append(path[::-1])
                    continue
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    if pattern not in adj:
                        continue
                    for prev in adj[pattern]:
                        if prev not in tree[word] and level + 1 <= dist[prev]:
                            dist[prev] = level + 1
                            if prev != beginWord:
                                tree[word].add(prev)
                            next_queue.append(path + [prev])
            if output:
                break
            queue = next_queue
        return output
