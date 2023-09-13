// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos, neg, zero = set(), set(), set()
        for i, num in enumerate(nums):
            (pos if num > 0 else neg if num < 0 else zero).add(i)

        output = []
        for i, j in combinations(pos, 2):
            complement = -(nums[i] + nums[j])
            if any(nums[idx] == complement for idx in neg):
                output.append((nums[neg[complement]], nums[i], nums[j]))
        for i, j in combinations(neg, 2):
            complement = -(nums[i] + nums[j])
            if complement in pos:
                output.append((nums[i], nums[j], nums[pos[complement]]))
        if len(zero) >= 3:
            output.append((0, 0, 0))

        return output