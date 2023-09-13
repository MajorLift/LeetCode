// https://leetcode.com/problems/high-five

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        for _id, score in items:
            if len(hashmap[_id]) < 5:
                heappush(hashmap[_id], score)
            elif score > hashmap[_id][0]:
                heappop(hashmap[_id])
                heappush(hashmap[_id], score)
                
        output = []
        for _id, heap in sorted(hashmap.items(), key=lambda x: x[0]):
            output.append([_id, int(sum(heap) / 5)])
        return output