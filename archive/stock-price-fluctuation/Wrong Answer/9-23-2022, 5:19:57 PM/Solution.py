// https://leetcode.com/problems/stock-price-fluctuation

class StockPrice:

    def __init__(self):
        self.latest_time = 0
        self.timepricemap = {} 
        self.minheap = []
        self.maxheap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timepricemap[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        heappush(self.minheap, (price, timestamp))
        heappush(self.maxheap, (-price, timestamp))

    def current(self) -> int:
        return self.timepricemap[self.latest_time]

    def maximum(self) -> int:
        while self.maxheap:
            price, timestamp = heappop(self.maxheap)
            if self.timepricemap[timestamp] == -price:
                return -price

    def minimum(self) -> int:
        while self.minheap:
            price, timestamp = heappop(self.minheap)
            if self.timepricemap[timestamp] == price:
                return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()