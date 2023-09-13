// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output, groups = [], defaultdict(list)
        for i,e in enumerate(groupSizes):
            groups[e].append(i)
        return [members[size * i : size * (i + 1)] 
            for size, members in groups.items() 
            for i in range(len(members) // size)]