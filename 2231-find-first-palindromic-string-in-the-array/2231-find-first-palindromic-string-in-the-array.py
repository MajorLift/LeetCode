class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next(filter(
                        lambda word: all(
                            l == r 
                            for l, r in zip(
                                word[:len(word) // 2 + 1], 
                                word[len(word) - 1:len(word) // 2 - 1:-1]
                            )), 
                        words),
                    "")