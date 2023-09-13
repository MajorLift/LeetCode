// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        maxAttack = max([attack for attack, defense in properties])

        maxDefense = [-inf] * (maxAttack + 2)
        for attack, defense in properties:
            maxDefense[attack] = max(maxDefense[attack], defense)
        maxDefense = list(accumulate(reversed(maxDefense), max))[::-1]

        return len([None 
            for attack, defense in properties 
            if defense < maxDefense[attack + 1]])