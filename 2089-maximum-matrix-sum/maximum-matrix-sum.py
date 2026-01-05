class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        mat_min = float('inf')
        neg_count = 0
        for row in matrix:
            for n in row:
                res += abs(n)
                if n < 0:
                    neg_count += 1
                mat_min = min(mat_min, abs(n))
        if neg_count % 2 != 0:
            res -= 2 * mat_min
        return res