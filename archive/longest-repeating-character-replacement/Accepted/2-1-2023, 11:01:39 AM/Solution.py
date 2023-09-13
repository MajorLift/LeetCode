// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freqs = defaultdict(int)
        max_len = 0
        l = r = 0
        while r < n:
            freqs[s[r]] += 1
            while sum(freqs.values()) - max(freqs.values()) > k:
                freqs[s[l]] -= 1
                l += 1
            else:
                max_len = max(max_len, r - l + 1)
                r += 1
        return max_len
