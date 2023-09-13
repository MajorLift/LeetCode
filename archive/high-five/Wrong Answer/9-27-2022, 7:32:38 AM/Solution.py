// https://leetcode.com/problems/high-five

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        for _id, score in items:
            heappush(hashmap[_id], -score)
        output = []
        for _id, heap in hashmap.items():
            output.append([_id, -int(sum(heap[:5]) / 5)])
        return output