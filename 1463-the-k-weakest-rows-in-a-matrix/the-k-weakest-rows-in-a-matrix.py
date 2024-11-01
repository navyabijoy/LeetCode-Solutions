class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = []
        for i, m in enumerate(mat):
            sol = (sum(m), i)
            temp.append(sol)

        temp.sort()
        return [i[1] for i in temp[:k]]