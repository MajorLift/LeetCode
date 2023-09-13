// https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = sorted(list(Counter(s).items()), key=lambda x: x[1])[::-1]
        return "".join(k * v for k, v in freqs)