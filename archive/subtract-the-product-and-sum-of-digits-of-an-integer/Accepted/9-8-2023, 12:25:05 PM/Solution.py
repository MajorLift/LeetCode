// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda acc, curr: acc * int(curr), str(n), 1) - sum(int(e) for e in str(n))