class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = [(sum(row), i) for i, row in enumerate(mat)]
        heapify(pq)
        return [i for cnt, i in nsmallest(k, pq)]