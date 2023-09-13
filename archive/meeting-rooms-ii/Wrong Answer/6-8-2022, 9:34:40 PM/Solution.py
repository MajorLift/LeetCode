// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        counter = 1
        # min_heap of ending times only
        end_times = [intervals[0][1]]
        # print(end_times)
        
        # iterate over intervals list and compare start_time to top of min_heap
        for [start, end] in intervals[1:]:
            # if start_time is geq than top than no need for new room
            # else need new room increment counter

            # poppush the corresponding end_time of curr interval into min_heap
            heapq.heapreplace(end_times, end)
            
            if start < end_times[0]:
                counter += 1
            
            # print(end_times)
            
        return counter