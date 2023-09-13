// https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while stones:
            if len(stones) == 1:
                return -heappop(stones)
            x, y = -heappop(stones), -heappop(stones)
            if x > y:
                heappush(stones, -(x - y))
        return 0