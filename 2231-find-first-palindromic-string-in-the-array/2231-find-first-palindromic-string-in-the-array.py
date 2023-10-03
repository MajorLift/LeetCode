class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return (list(filter(self.isPalindrome, words)) or [""])[0]
    
    def isPalindrome(self, word: str) -> bool:
        return all(l == r for l, r in zip(word, reversed(word)))