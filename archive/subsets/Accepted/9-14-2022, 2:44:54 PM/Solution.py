// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            queue = deque(output)
            while queue:
                curr = queue.popleft().copy()
                curr.append(num)
                output.append(curr)
        return output