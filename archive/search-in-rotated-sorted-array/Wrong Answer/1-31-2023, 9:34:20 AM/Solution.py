// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                pivot = i
                break
        res = bisect_right([i for i in range(n)], target, key=lambda x: nums[(x + pivot) % n])
        res = (res - pivot) % n
        return res if nums[res] == target else -1