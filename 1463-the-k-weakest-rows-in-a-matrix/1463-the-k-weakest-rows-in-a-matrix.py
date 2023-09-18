class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = [(sum(row), i) for i, row in enumerate(mat)]
        return [i for cnt, i in nsmallest(k, pq)]