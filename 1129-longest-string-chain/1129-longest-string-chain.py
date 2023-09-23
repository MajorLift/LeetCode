class Solution:
    def longestStrChain(self, words) -> int:
        memo = defaultdict(int)
        for word in sorted(words, key=len):
            memo[word] = 1 + max(memo[word[:i] + word[i + 1:]] 
                                for i in range(len(word)))
        return max(memo.values())