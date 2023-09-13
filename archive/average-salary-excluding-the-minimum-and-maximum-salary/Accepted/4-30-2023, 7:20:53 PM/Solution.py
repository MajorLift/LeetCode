// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary

class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        _max, _min, _sum = -inf, +inf, 0
        for num in salary:
            _max, _min = max(_max, num), min(_min, num)
            _sum += num
        return (_sum - (_max + _min)) / (n - 2)