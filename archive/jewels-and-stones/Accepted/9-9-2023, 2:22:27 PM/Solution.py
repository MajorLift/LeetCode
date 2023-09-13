// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return ((jewels_set := set(jewels)), sum(stone in jewels_set for stone in stones))[1]