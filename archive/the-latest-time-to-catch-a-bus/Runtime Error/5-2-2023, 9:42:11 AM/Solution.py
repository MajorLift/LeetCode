// https://leetcode.com/problems/the-latest-time-to-catch-a-bus

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        
        idx, avail = 0, +inf
        for time in buses:
            avail = capacity
            while avail > 0 \
                and passengers[idx] <= time \
                and idx < len(passengers):
                avail -= 1
                idx += 1
        
        slot = buses[-1]
        if avail == 0:
            slot = passengers[idx - 1]
        while slot in set(passengers):
            slot -= 1
        return slot