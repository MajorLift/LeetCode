// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        odd = False
        if (m+n) % 2 == 1:
            odd = True
        limit = int((m+n) // 2)
            
        merged = []
        
        i = 0
        j = 0
        idx = 0
        while idx <= limit:
            while i < m and j < n and nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
                idx += 1
            while i < m and j < n and nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j += 1
                idx += 1
        
        if odd:
            return float(merged[limit])
        else:
            return (merged[limit] + merged[limit-1]) / 2
        
            