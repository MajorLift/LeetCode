class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairOf = {**{x: y for x, y in pairs}, **{y: x for x, y in pairs}}
        return sum(
            any(x in U.getPreferredOver(v) 
                for u in X.getPreferredOver(y)
                    if (U := Person(preferences[u]), v := pairOf[u]))
            for x in range(n)
                    if (X := Person(preferences[x]), y := pairOf[x]))

class Person:
    def __init__(self, preference):
        self.preference = preference
    
    def getPreferredOver(self, this):
        return set(self.preference[:self.preference.index(this)])