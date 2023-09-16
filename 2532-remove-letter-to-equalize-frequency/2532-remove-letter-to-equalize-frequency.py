class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(Counter(word).values())
        return len(cnt) == 2 and (cnt[1] == 1 or cnt[min(cnt) + 1] == 1) \
            or len(cnt) == 1 and (1 in cnt or 1 in cnt.values())