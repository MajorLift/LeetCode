class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0] * 26
        for char in magazine:
            cnt[ord(char) - ord('a')] += 1
        for char in ransomNote:
            cnt[ord(char) - ord('a')] -= 1
            if cnt[ord(char) - ord('a')] < 0:
                return False
        return True