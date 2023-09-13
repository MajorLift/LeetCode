// https://leetcode.com/problems/max-pair-sum-in-an-array

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, e in enumerate(nums):
            max_digit = 0
            while e:
                emax = 10 ** int(math.log10(e))
                msd = e // emax
                e -= msd * emax
                max_digit = max(max_digit, msd)
            d[max_digit].append(i)

        return max([nums[l] + nums[r] for k in d for l, r in combinations(d[k], 2)] or [-1])