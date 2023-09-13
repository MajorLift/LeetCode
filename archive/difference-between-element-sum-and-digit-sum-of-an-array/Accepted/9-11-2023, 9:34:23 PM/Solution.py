// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_iter(nums):
            while nums:
                curr = nums.pop()
                pos = 10 ** int(math.log10(curr))
                yield curr // pos
                curr -= (curr // pos) * pos
                if curr:
                    nums.append(curr)
        return abs(sum(nums) - sum(digit_iter(nums)))
