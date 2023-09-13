// https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, char in enumerate(s):
            last[char] = i

        output = []
        size = end = 0
        for i, char in enumerate(s):
            size += 1
            end = max(end, last[char])
            if i == end:
                output.append(size)
                size = 0
        return output