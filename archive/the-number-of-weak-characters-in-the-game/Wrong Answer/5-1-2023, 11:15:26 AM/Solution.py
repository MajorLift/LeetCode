// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        props = sorted(properties, key=lambda x: x[0])
        ans = 0
        for i in range(n - 1):
            j = i
            while j < n and props[j][0] == props[i][0]:
                j += 1
            for k in range(j, n):
                ans += 1 if props[k][1] > props[i][1] else 0
        return ans