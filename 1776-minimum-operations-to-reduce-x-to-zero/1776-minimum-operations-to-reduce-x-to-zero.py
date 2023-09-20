class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n, l, win_sum, win_size, target = len(nums), -1, 0, -1, sum(nums) - x
        for r, num in enumerate(nums):
            win_sum += num
            while l + 1 < n and win_sum > target:
                l += 1
                win_sum -= nums[l]
            if win_sum == target:
                win_size = max(win_size, r - l)
        return n - win_size if win_size >= 0 else -1