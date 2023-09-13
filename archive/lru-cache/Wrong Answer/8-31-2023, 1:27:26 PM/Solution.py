// https://leetcode.com/problems/lru-cache

class LRUCache:

    def __init__(self, capacity: int):
        self.clock = 0
        self.capacity = capacity
        self.cache = dict() # K: v
        self.pq = [] # time[]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        for i, (time, k) in enumerate(self.pq):
            if k == key:
                self.pq.pop(i)
        heappush(self.pq, (self.clock, key))
        self.clock += 1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        
        for i, (time, k) in enumerate(self.pq):
            if k == key:
                self.pq.pop(i)
        heappush(self.pq, (self.clock, key))
        self.clock += 1

        if len(self.cache) > self.capacity:
            time, k = heappop(self.pq)
            del self.cache[k]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)