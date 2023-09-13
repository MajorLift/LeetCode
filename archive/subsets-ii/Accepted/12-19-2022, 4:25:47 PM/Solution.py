// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        for i in range(len(nums)):
            start_idx = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start_idx = prev_subsets
            prev_subsets = len(subsets)
            queue = deque(subsets[start_idx:])
            while queue:
                curr = queue.popleft().copy()
                curr.append(nums[i])
                subsets.append(curr)
        return subsets