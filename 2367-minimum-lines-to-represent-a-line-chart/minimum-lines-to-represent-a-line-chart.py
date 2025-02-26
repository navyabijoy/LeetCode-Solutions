class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        n = len(stockPrices)
        if n == 1:
            return 0
        line = 1
        for i in range(1,n-1):
            point1, point2, point3 = stockPrices[i-1],stockPrices[i],stockPrices[i+1]
            t1 = (point2[1] - point1[1]) * (point3[0] - point1[0])
            t2 = (point3[1] - point1[1]) * (point2[0] - point1[0])
            if t1 != t2:
                line += 1
        return line
        