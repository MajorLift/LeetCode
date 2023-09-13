// https://leetcode.com/problems/task-scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = collections.Counter(tasks)
        maxFreq = max(freqs.values())
        numTies = len([k for k,v in freqs.items() if v == maxFreq])
        return max(len(tasks), (maxFreq - 1) * (n + 1) + numTies)