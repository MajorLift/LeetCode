// https://leetcode.com/problems/random-pick-with-blacklist

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.blacklist = set(blacklist)
        self.candidates = [num for num in range(self.n) if num not in self.blacklist]
        self.k = len(self.candidates)

    def pick(self) -> int:
        return self.candidates[int(random.random() * self.k)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()