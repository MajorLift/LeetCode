// https://leetcode.com/problems/minimum-increment-to-make-array-unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        dups = set([k for k, v in cnt.items() if v > 1])
        # print(dups)
        ans = 0
        while dups:
            for dup in [*dups]:
                cnt[dup] -= 1
                if cnt[dup] == 1:
                    dups.remove(dup)
                if dup + 1 in cnt:
                    cnt[dup + 1] += 1
                    dups.add(dup + 1)
                else:
                    cnt[dup + 1] = 1
                ans += 1
        return ans