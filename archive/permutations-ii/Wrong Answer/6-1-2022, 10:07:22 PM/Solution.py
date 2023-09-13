// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        def backtrack(first = 0):
            if first == n:
                output.append(nums[:])
            else:
                lookup = set()
                for i in range(first, n):
                    if nums[i] not in lookup:
                        nums[first], nums[i] = nums[i], nums[first]
                        backtrack(i + 1)
                        nums[first], nums[i] = nums[i], nums[first]
                        lookup.add(nums[i])
                    
        backtrack()
        return output