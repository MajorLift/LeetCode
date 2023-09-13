// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        num_prev_subsets = 0
        for i, num in enumerate(nums):
            start_idx = num_prev_subsets if i > 0 and num == nums[i - 1] else 0
            num_prev_subsets = len(subsets)
            queue = deque(subsets[start_idx:])
            while queue:
                curr = queue.popleft().copy()
                curr.append(num)
                subsets.append(curr)
        return subsets
