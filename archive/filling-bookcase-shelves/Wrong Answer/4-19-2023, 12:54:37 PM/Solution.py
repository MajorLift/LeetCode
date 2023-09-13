// https://leetcode.com/problems/filling-bookcase-shelves

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        books.sort(key=lambda x: (x[1], x[0]))
        widths, heights = map(list, zip(*books))
        ans = 0
        while widths:
            i = bisect_right(list(accumulate(widths, operator.add)), shelfWidth)
            ans += heights[i - 1]
            widths, heights = widths[i:], heights[i:]
            print(i, widths, heights)
        return ans
