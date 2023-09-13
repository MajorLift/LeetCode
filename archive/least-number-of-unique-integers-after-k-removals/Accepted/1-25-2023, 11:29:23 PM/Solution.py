// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        pq = [v for v in cnt.values()]
        heapify(pq)
        while pq and k > 0:
            count = heappop(pq)
            k -= count
        return len(pq) + (0 if k >= 0 else 1)