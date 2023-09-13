// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        if n >= 3:
            nums.sort()
            for i in range(n - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                    continue
                if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                    break
            
                a = nums[i]
                j = i + 1
                k = n - 1
                while j < k:
                    b, c = nums[j], nums[k]
                    if b + c == -a: 
                        results.append([a, b, c])
                        while nums[j] == nums[j + 1]:
                            j += 1
                        j += 1
                        while nums[k] == nums[k - 1]:
                            k -= 1
                        k -= 1
                    elif b + c > -a:
                        k -= 1
                    elif b + c < -a:
                        j += 1
        return results