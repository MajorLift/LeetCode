class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word: str) -> bool:
            n = len(word)
            return all(l == r for l, r in zip(word[:n // 2], reversed(word[n // 2:])))
        return (list(filter(isPalindrome, words)) or [""])[0]
        