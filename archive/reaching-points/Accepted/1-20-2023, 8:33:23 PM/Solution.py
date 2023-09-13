// https://leetcode.com/problems/reaching-points

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx > ty:
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx %= ty
            elif tx < ty:
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty %= tx
            else:
                break
        return tx == sx and ty == sy