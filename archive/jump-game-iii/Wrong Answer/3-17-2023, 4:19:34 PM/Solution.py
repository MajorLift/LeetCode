// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n, visited = len(arr), set()
        def jump(i):
            if i in visited or len(visited) == n:
                return False
            visited.add(i)
            return arr[i] == 0 \
                or jump(max(0, i - arr[i])) \
                or jump(min(n - 1, i + arr[i]))
        return jump(start)