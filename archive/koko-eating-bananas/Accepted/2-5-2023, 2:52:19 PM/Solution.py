// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(max(piles) + 1), True, lo=1, 
            key=lambda k: sum([math.ceil(piles[i] / k) for i in range(len(piles))]) <= h)