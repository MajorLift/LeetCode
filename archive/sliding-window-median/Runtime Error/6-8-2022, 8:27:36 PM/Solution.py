// https://leetcode.com/problems/sliding-window-median

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        
        # initialize heap with k elems
        lo, hi = [], []
        for i in range(k):
            heapq.heappush(lo, -nums[i])
        for j in range(k // 2):
            heapq.heappush(hi, -heapq.heappop(lo))
        medians.append(-lo[0] if k % 2 > 0 else (-lo[0] + hi[0]) / 2)
        
        balance = 0
        invalidated = {num: 0 for num in nums}
        # iterate over remainder of nums and populate medians
        for head_idx in range(k, len(nums)):
            in_num, out_num = nums[head_idx], nums[head_idx - k]
            # print(in_num, out_num)
            
            # exit
            if out_num <= -lo[0]:
                balance -= 1
            else:
                balance += 1
            invalidated[out_num] += 1
                
            # enter
            if len(lo) > 0 and in_num <= -lo[0]:
                heapq.heappush(lo, -in_num)
                balance += 1
            else:
                heapq.heappush(hi, in_num)
                balance -= 1
            
            # balance
            if balance < 0:
                heapq.heappush(lo, -heapq.heappop(hi))
                balance += 1
            elif balance > 0:
                heapq.heappush(hi, -heapq.heappop(lo))
                balance -= 1
                
            # removed
            while invalidated[-lo[0]] > 0:
                invalidated[-lo[0]] -= 1
                heapq.heappop(lo)
            while invalidated[hi[0]] > 0:
                invalidated[hi[0]] -= 1
                heapq.heappop(hi)
                
            medians.append(-lo[0] if k % 2 > 0 else (-lo[0] + hi[0]) / 2)
            # print(medians[-1])
            
        return medians