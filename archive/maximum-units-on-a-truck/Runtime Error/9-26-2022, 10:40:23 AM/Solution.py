// https://leetcode.com/problems/maximum-units-on-a-truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        pq = []
        for [numBoxes, numUnits] in boxTypes:
            heappush(pq, (-numUnits, numBoxes))
        boxesTotal, unitsTotal = truckSize, 0
        while boxesTotal > 0:
            units, boxes = heappop(pq)
            units *= -1
            putOnTruck = boxes if boxesTotal > boxes else boxesTotal
            boxesTotal -= putOnTruck
            unitsTotal += putOnTruck * units
        return unitsTotal