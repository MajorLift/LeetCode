class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        positive_set, negative_heap = set(), []
        for num in nums:
            if num > 0:
                positive_set.add(num)
            else:
                heappush(negative_heap, num)
        while negative_heap:
            candidate = heappop(negative_heap)
            if -candidate in positive_set:
                return -candidate
        return -1