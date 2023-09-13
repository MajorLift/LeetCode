// https://leetcode.com/problems/minimum-time-to-make-rope-colorful

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        self.n = len(colors)
        self.costs = neededTime
        self.colors = list(colors)
        self.find_clusters()
        # print(self.clusters)
        return sum(self.remove_all_but_max(l, r) for l, r in self.clusters)
        
    def find_clusters(self):
        self.clusters = []
        for l in range(self.n):
            r = l
            while r < self.n and self.colors[l] == self.colors[r]:
                r += 1
            if r > l + 1:
                self.clusters.append((l, r))

    def remove_all_but_max(self, start: int, end: int) -> int:
        return sum(self.costs[start:end]) - max(self.costs[start:end])