// https://leetcode.com/problems/top-k-frequent-words

from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        pq = [(-freq, word) for word,freq in cnt.items()]
        heapq.heapify(pq)
        output = []
        while pq and len(output) < k:
            output.append(heapq.heappop(pq)[1])
        return output