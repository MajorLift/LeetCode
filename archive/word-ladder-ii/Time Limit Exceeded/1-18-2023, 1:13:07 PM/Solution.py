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
        curr_dist = 0

        queue = deque([(endWord, [endWord])])
        while queue:
            curr_dist += 1
            next_queue = deque()
            while queue:
                word, path = queue.popleft()
                if word == beginWord:
                    if curr_dist == dist[word]:
                        output.append(path[::-1])
                    elif curr_dist < dist[word]:
                        dist[word] = curr_dist
                        output = [path[::-1]]
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in (adj[pattern] if pattern in adj else []):
                        if curr_dist + 1 <= dist[neighbor]:
                            dist[neighbor] = curr_dist + 1
                            next_queue.append((neighbor, path + [neighbor]))
            queue = next_queue
        return output