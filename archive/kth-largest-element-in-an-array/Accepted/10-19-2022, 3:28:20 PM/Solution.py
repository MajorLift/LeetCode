// https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            else:
                heapq.heappushpop(minheap, num)
        return minheap[0]