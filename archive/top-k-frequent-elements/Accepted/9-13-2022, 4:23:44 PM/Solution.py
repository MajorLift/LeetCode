// https://leetcode.com/problems/top-k-frequent-elements

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        heap = [[-v, k] for [k, v] in hashmap.items()]
        heapq.heapify(heap)
        # print(heap)
        # print(heapq.nsmallest(k, heap))
        return [pair[1] for pair in heapq.nsmallest(k, heap)]