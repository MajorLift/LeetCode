class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            if len(nums) > 1:
                first, last = nums.pop(0), nums.pop()
                ans += first * 10 ** int(math.log10(last) + 1) + last
            else:
                ans += nums.pop()                
        return ans