// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        for i in range(len(nums)):
            queue = deque(subsets[prev_subsets:] if i > 0 and nums[i] == nums[i - 1] else subsets)
            prev_subsets = len(subsets)
            while queue:
                curr = queue.popleft().copy()
                curr.append(nums[i])
                subsets.append(curr)
        return subsets