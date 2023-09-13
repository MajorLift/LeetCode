// https://leetcode.com/problems/guess-the-word

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        response = 0
        while words and response < 6:
            query = words[random.randrange(len(words))]
            response = master.guess(query)
            words = [word for word in words 
                if self.matches(word, query) == response]

    def matches(self, a, b):
        return len([a[i] == b[i] for i in range(6)])