// https://leetcode.com/problems/filling-bookcase-shelves

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        widths, heights = map(list, zip(*books))
        ans = 0
        while widths:
            i = bisect_right(list(accumulate(widths, operator.add)), shelfWidth + 1)
            ans += max(heights[:i])
            print(i, widths, heights)
            widths, heights = widths[i:], heights[i:]
        return ans
