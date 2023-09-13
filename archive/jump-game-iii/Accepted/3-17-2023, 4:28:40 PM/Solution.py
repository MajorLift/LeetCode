// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n, visited = len(arr), set()
        def jump(i):
            if 0 <= i < n and i not in visited:
                visited.add(i)
                return (arr[i] == 0
                    or jump(i - arr[i])
                    or jump(i + arr[i]))
        return jump(start)