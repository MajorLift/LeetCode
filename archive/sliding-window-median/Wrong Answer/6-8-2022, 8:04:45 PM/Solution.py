// https://leetcode.com/problems/sliding-window-median

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # initialize heaps
        lo, hi = [], []
        for i in range(k):
            heapq.heappush(lo, -nums[i])
        for j in range(k // 2):
            heapq.heappush(hi, -heapq.heappop(lo))
        
        medians = []
        invalid = {}
        for num in nums:
            if num not in invalid.keys():
                invalid[num] = 0
            else:
                invalid[num] += 1
        balance = 0
        
        for head in range(k, len(nums)):
            print(head)
            medians.append(-lo[0] if k % 2 > 0 \
                else (-lo[0] + hi[0]) / 2)
            print(medians[-1])
            
            in_num, out_num = nums[head], nums[head - k]
            print(in_num, out_num)
            
            # exit
            invalid[out_num] += 1
            if out_num <= -lo[0]:
                balance -= 1
            elif len(hi) > 0 and out_num > hi[0]:
                balance += 1
            
            # enter
            if len(lo) > 0 and in_num <= -lo[0]:
                heapq.heappush(lo, -in_num)
                balance += 1
            else:
                heapq.heappush(hi, in_num)
                balance -= 1
            
            # re-balance
            if balance < 0:
                heapq.heappush(lo, -heapq.heappop(hi))
                balance += 1
            elif balance > 0:
                heapq.heappush(hi, -heapq.heappop(lo))
                balance -= 1
            
            # remove
            lo_top, hi_top = -lo[0], hi[0] if len(hi) > 0 else None
            while invalid[lo_top] > 0:
                heapq.heappop(lo)
                invalid[lo_top] -= 1
            while len(hi) > 0 and invalid[hi_top] > 0:
                heapq.heappop(hi)
                invalid[hi_top] -= 1
            
            print(lo, hi, balance)
            print(invalid)
            
        return medians