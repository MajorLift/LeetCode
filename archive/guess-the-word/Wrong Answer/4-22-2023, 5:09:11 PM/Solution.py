// https://leetcode.com/problems/guess-the-word

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        i = response = 0
        while i := i + 1 < 10 and response < 6:
            query = words[random.randrange(len(words))]
            response = master.guess(query)
            words = list(filter(lambda x: self.matches(x, query) == response, words))

    def matches(self, a, b):
        return len(list(filter(lambda x: x[0] == x[1], zip(a, b))))