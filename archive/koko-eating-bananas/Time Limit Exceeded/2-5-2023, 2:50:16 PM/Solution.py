// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for k in range(1, max(piles) + 1):
            if sum([math.ceil(piles[i] / k) for i in range(len(piles))]) <= h:
                return k