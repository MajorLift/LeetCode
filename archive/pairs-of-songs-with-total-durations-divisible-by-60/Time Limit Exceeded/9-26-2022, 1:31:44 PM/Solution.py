// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rems = [x % 60 for x in time]
        count = 0
        for i in range(len(time) - 1):
            complement = (60 - rems[i]) % 60
            for j in range(i + 1, len(time)):
                if rems[j] == complement:
                    count += 1
        return count