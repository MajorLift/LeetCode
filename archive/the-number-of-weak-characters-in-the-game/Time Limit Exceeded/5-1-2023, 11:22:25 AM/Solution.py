// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n, props = len(properties), sorted(properties)
        ans = 0
        for i in range(n - 1):
            j = i + 1
            while j < n and props[j][0] == props[i][0]:
                j += 1
            ans += 1 \
                if any(props[k][1] > props[i][1] 
                    for k in range(j, n)) \
                else 0
        return ans