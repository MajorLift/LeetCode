// https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, char in enumerate(s):
            last[char] = i

        output = []
        l = r = 0
        for i, char in enumerate(s):
            r = max(r, last[char])
            if i == r:
                output.append(r - l + 1)
                l = r = r + 1
        return output