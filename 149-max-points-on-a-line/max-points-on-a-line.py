class Solution:
    def maxPoints(self, point: List[List[int]]) -> int:
        n = len(point)
        if(n<=2):
            return n
        result = 2
        for i in range(n):
            for j in range(i+1,n):
                count = 2
                for k in range(j+1,n):
                    t1 = (point[j][1] - point[i][1]) * (point[k][0] - point[i][0])
                    t2 = (point[k][1] - point[i][1]) * (point[j][0] - point[i][0])
                    if(t1 == t2):
                        count += 1
                result = max(count, result)
        return result
            
