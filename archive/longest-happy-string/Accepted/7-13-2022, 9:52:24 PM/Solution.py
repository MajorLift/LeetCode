// https://leetcode.com/problems/longest-happy-string

class Solution:
    def longestDiverseString(self, *args) -> str:
        max_heap = []
        for i, arg in enumerate(args):
            if arg > 0:
                heapq.heappush(max_heap, (-arg, chr(ord('a') + i)))
        # print(max_heap)
        s = []
        while True:
            if not max_heap:
                break
            first, char1 = heapq.heappop(max_heap)
            if len(s) >= 2 and s[-1] == s[-2] == char1:
                if not max_heap:
                    break
                second, char2 = heapq.heappop(max_heap)
                s.append(char2)
                second += 1
                if second < 0:
                    heapq.heappush(max_heap, (second, char2))
                heapq.heappush(max_heap, (first, char1))
            else:
                s.append(char1)
                first += 1
                if first < 0:
                    heapq.heappush(max_heap, (first, char1))
            # print(s, max_heap)
        return ''.join(s)