class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(Counter(word).values())
        return len(cnt) == 1 and 1 in (min(cnt), cnt[min(cnt)]) \
            or len(cnt) == 2 and 1 in (cnt[1], cnt[min(cnt) + 1])
