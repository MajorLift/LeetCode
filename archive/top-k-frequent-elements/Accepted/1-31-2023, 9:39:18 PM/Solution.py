// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pairs = sorted(list(Counter(nums).items()), key=lambda x: -x[1])[:k]
        return [pair[0] for pair in pairs]