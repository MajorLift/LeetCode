class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_iter(nums: List[int]):
            while nums:
                curr = nums.pop()
                yield curr % 10
                curr //= 10
                if curr:
                    nums.append(curr)
        return abs(sum(nums) - sum(digit_iter(nums)))