// https://leetcode.com/problems/word-ladder-ii

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList + [beginWord])
        if endWord not in words:
            return []

        adj = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)

        tree = defaultdict(set)
        dist = defaultdict(lambda: +math.inf)
        dist[endWord] = 0
        level = 0
        queue = deque([endWord])
        flag = False
        while queue:
            level += 1
            next_queue = deque()
            while queue:
                word = queue.popleft()
                if word == beginWord:
                    flag = True
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    if pattern not in adj:
                        continue
                    for prev in adj[pattern]:
                        if level + 1 <= dist[prev]:
                            dist[prev] = level + 1
                            tree[prev].add(word)
                            next_queue.append(prev)
            if flag:
                break
            queue = next_queue
        
        output = []
        stack = [[beginWord]]
        while stack:
            path = stack.pop()
            word = path[-1]
            if word == endWord:
                output.append(path)
            for next_word in tree[word]:
                stack.append(path + [next_word])
        return output