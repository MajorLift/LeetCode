// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum, digit_sum = sum(nums), 0
        while nums:
            curr = nums.pop()
            pos = 10 ** int(math.log10(curr))
            digit_sum += curr // pos
            curr -= (curr // pos) * pos
            if curr:
                nums.append(curr)
        return abs(elem_sum - digit_sum)
