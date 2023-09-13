// https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hashmap = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.arr.append(val)
        self.hashmap[val] = self.length
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        idx = self.hashmap[val]
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop()
        self.length -= 1
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()