// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return ((jewels_set := set(jewels)), len(list(filter(lambda stone: stone in jewels_set, stones))))[-1]