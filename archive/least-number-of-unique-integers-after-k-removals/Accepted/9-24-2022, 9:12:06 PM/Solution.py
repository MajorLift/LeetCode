// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = defaultdict(int)
        for num in arr:
            freqs[num] += 1
            
        pq = []
        for num, freq in freqs.items():
            heappush(pq, (freq, num))
        while k > 0:
            curr_freq, curr_num = heappop(pq)
            if curr_freq > 1:
                heappush(pq, (curr_freq - 1, curr_num))
            k -= 1
        return len(pq)