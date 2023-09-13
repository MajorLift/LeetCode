// https://leetcode.com/problems/reaching-points

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx < sx or ty < sy:
            return False

        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
                
        return (tx == sx and ty == sy) \
            or (tx == sx and (ty - sy) % tx == 0) \
            or (ty == sy and (tx - sx) % ty == 0)