// https://leetcode.com/problems/group-anagrams

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        groups = defaultdict(list)
        for s in strs:
            freqs = [0] * 26
            for char in s:
                freqs[ord(char.lower()) - ord('a')] += 1
            groups["#".join([str(num) for num in freqs])].append(s)
        return groups.values()
            