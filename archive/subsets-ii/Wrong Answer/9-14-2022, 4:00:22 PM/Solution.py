// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i, num in enumerate(nums):
            start_idx = 0
            if i > 0 and num == nums[i - 1]:
                start_idx = num_prev_subsets
            queue = deque(subsets[start_idx:])
            while queue:
                curr = queue.popleft().copy()
                curr.append(num)
                subsets.append(curr)
            num_prev_subsets = len(subsets) // 2
        return subsets
