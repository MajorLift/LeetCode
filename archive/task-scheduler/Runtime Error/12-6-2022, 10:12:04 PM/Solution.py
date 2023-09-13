// https://leetcode.com/problems/task-scheduler

def leastInterval(self, tasks: List[str], n: int) -> int:
    freqs = collections.Counter(tasks)
    maxFreq = max(freqs.values())
    numMax = len([v for v in freqs.values() if v == maxFreq])
    return max(len(tasks), (maxFreq - 1) * (n + 1) + numMax)