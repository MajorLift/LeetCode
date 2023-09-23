class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        memo = defaultdict(int)
        for word in words:
            memo[word] = 1 + max(memo[word[:i] + word[i + 1:]]
                                for i in range(len(word)))
        return max(memo.values())