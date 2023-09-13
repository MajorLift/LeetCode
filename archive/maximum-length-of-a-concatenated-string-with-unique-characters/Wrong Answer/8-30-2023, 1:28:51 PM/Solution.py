// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        lens = list(map(len, arr))
        max_len = 0
        for k in range(1, n + 1):
            for idxs in combinations(range(n), k):
                unique_chars = set()
                is_all_unique = True
                for idx in idxs:
                    idx_chars = set(arr[idx])
                    if unique_chars & idx_chars:
                        is_all_unique = False
                        break
                    unique_chars |= idx_chars
                if is_all_unique:
                    max_len = max(max_len, sum(lens[i] for i in idxs))
        return max_len
            