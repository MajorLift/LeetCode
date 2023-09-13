// https://leetcode.com/problems/minimum-penalty-for-a-shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_val, min_idx = min(
            ((sum([int(e == "N") for e in customers[:j]] + [int(e == "Y") for e in customers[j:]]), j) 
                for j in range(len(customers) + 1)), 
            key=lambda x: x[0])
        return min_idx