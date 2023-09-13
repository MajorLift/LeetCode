// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnts = [Counter(word) for word in strs]
        output = [[word] for word in strs]
        for i, j in combinations(range(len(strs)), 2):
            if cnts[i] == cnts[j]:
                output[i] += output[j]
                output[j] = []
        return [group for group in output if group]