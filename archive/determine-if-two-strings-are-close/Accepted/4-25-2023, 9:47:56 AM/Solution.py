// https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = map(Counter, (word1, word2))
        return set(cnt1.keys()) == set(cnt2.keys()) \
            and sorted(cnt1.values()) == sorted(cnt2.values())