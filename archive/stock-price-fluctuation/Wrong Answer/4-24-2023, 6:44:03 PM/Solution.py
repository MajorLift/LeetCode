// https://leetcode.com/problems/stock-price-fluctuation

class StockPrice:

    def __init__(self):
        self.records = dict()
        self.corrected = set()
        self.maxheap, self.minheap = [], []
        self.latest = -inf

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.records:
            self.corrected.add(self.records[timestamp])
        else:
            self.latest = timestamp
            if price in self.corrected:
                self.corrected.remove(price)
        self.records[timestamp] = price
        heappush(self.maxheap, -price)
        heappush(self.minheap, price)

    def current(self) -> int:
        return self.records[self.latest]

    def maximum(self) -> int:
        while -self.maxheap[0] in self.corrected:
            heappop(self.maxheap)
        return -self.maxheap[0]

    def minimum(self) -> int:
        while self.minheap[0] in self.corrected:
            heappop(self.minheap)
        return self.minheap[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()