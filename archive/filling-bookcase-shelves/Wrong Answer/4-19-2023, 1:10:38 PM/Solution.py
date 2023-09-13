// https://leetcode.com/problems/filling-bookcase-shelves

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        widths, heights = map(list, zip(*books))
        ans = 0
        while widths:
            widths_acc = list(accumulate(widths, operator.add))
            i = bisect_right(widths_acc, shelfWidth)
            if i >= len(widths_acc):
                break
            if widths_acc[i] == shelfWidth:
                i += 1
            ans += max(heights[:i])
            print(i, widths, heights)
            widths, heights = widths[i:], heights[i:]
        return ans
