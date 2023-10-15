class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        people = {i: Person(e) for i, e in enumerate(preferences)}
        pair = {**{x: y for x, y in pairs}, **{y: x for x, y in pairs}}
        ans = 0
        for x in range(n):
            for u in people[x].getPreferredThan(pair[x]):
                if x in people[u].getPreferredThan(pair[u]):
                    ans += 1
                    break
        return ans

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredThan(self, this):
        return set(self.preference[:self.preference.index(this)])