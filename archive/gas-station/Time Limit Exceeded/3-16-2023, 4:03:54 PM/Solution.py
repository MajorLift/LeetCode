// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        arr = list(zip(gas, cost))
        for start in range(n):
            tank = 0
            for i in range(n):
                g, c = arr[(start + i) % n]
                tank = tank + g - c
                if tank < 0:
                    break
            if tank >= 0:
                return start
        return -1
            