class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairOf = {**{x: y for x, y in pairs}, **{y: x for x, y in pairs}}
        return sum(
            any(x in Person(preferences[u]).getPreferredThan(pairOf[u]) 
                for u in Person(preferences[x]).getPreferredThan(pairOf[x])) 
            for x in range(n))

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredThan(self, this):
        return set(self.preference[:self.preference.index(this)])