// https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        queue = [[num] for num in nums]
        while len(queue) > 0:
            left = queue.pop(0)
            if len(queue) == 0:
                return left
            elif len(left) > len(queue[0]):
                queue.append(left)
            else:      
                right = queue.pop(0)
                merged = []
                j, k = 0, 0
                while j < len(left) or k < len(right):
                    if k == len(right) or (j < len(left) and left[j] <= right[k]):
                        merged.append(left[j])
                        j += 1
                    elif j == len(left) or (k < len(right) and left[j] > right[k]):
                        merged.append(right[k])
                        k += 1
                queue.append(merged)