// https://leetcode.com/problems/filling-bookcase-shelves

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        books.sort(key=lambda x: (x[1], x[0]))
        books = accumulate(books, lambda acc, curr: [sum(acc[0] + curr[0]), max(acc[1], curr[1])])
        print(books)

        # ans = 0
        # while books:
        #     idx = bisect_left(a=books, x=shelfWidth)
        #     ans += books[idx][1]
        #     books = books[idx+1:]
        # return ans