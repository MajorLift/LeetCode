// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output, groups = [], defaultdict(list)
        for i,e in enumerate(groupSizes):
            groups[e].append(i)
        for size, members in groups.items():
            while members:
                output.append(members[:size])
                members = members[size:]
        return output