class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target, source = map(sorted, (ransomNote, magazine))
        m, n = map(len, (target, source))
        i = j = 0
        while True:
            if i == m:
                return True
            if j == n:
                return False
            while i < m and j < n and target[i] == source[j]:
                i += 1
                j += 1
            while i < m and j < n and target[i] != source[j]:
                j += 1
