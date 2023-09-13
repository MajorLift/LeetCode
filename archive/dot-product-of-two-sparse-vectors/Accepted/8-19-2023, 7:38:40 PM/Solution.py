// https://leetcode.com/problems/dot-product-of-two-sparse-vectors

class SparseVector:
    def __init__(self, nums: List[int]):
        self.obj = {i: e for i,e in enumerate(nums) if e != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(self.obj[idx] * vec.obj[idx] for idx in self.obj.keys() & vec.obj.keys())

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)