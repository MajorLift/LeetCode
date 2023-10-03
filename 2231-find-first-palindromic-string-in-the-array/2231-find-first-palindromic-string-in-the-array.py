class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word: str) -> bool:
            return all(l == r for l, r in zip(word, reversed(word)))
        return (list(filter(isPalindrome, words)) or [""])[0]
        