// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len(re.compile(f'[{jewels}]').findall(stones))