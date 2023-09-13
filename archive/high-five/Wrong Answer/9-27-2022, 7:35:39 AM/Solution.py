// https://leetcode.com/problems/high-five

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        for _id, score in items:
            heappush(hashmap[_id], -score)
        output = []
        for _id, heap in hashmap.items():
            topFiveSum = 0
            for i in range(5):
                topFiveSum += heappop(heap)
            output.append([_id, int(-topFiveSum / 5)])
        return output