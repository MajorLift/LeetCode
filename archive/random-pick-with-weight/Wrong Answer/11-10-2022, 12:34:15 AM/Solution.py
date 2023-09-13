// https://leetcode.com/problems/random-pick-with-weight

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.len = len(w)
        self.sum = sum(w)
        self.prefix = [w[0]] + [0] * (self.len - 1)
        for i in range(1, self.len):
            self.prefix[i] += self.prefix[i - 1]

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.prefix, random.random() * self.sum) // self.sum


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()