// https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:

    def __init__(self):
        self.maxheap, self.minheap = [], []

    def addNum(self, num: int) -> None:
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

    def findMedian(self) -> float:
        if not self.maxheap:
            return self.minheap[0]
        if len(self.minheap) > len(self.maxheap):
            return -self.maxheap[0]
        elif len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()