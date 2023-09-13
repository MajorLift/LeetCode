// https://leetcode.com/problems/separate-the-digits-in-an-array

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = deque()
        while nums:
            curr = nums.pop()
            output.appendleft(curr % 10)
            curr //= 10
            if curr:
                nums.append(curr)
        return output