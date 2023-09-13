// https://leetcode.com/problems/maximum-population-year

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        updates = []
        for birth, death in logs:
            updates.append((birth, +1))
            updates.append((death, -1))
        updates.sort()
        
        population = max_pop = max_year = 0
        for year, diff in updates:
            population += diff
            if population > max_pop:
                max_pop = population
                max_year = year
        return max_year