// https://leetcode.com/problems/filling-bookcase-shelves

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        books.sort(key=lambda x: (x[1], x[0]))
        widths, heights = zip(*books)
        widths = accumulate(widths, sum)
        heights = accumulate(heights, max)
        books = zip(widths, heights)
        print(*books)
        
        # ans = 0
        # while books:
        #     idx = bisect_left(a=books, x=shelfWidth)
        #     ans += books[idx][1]
        #     books = books[idx+1:]
        # return ans