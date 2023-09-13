// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        count = 0
        for t in time:
            count += remainders[(60 - t) % 60]
            remainders[t % 60] += 1
        return count