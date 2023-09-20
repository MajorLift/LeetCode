class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            if len(nums) > 1:
                first, last = nums.pop(0), nums.pop()
                first *= 10 ** (math.floor(math.log10(last)) + 1)
                first += last
                ans += first
            else:
                ans += nums.pop()                
        return ans