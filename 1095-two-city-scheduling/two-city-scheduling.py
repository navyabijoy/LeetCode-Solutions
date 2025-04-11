class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for c1,c2 in costs:
            diff.append([c1-c2,c1,c2])
        diff.sort() # sort the difference between the cost of the city
        res = 0
        for i in range(len(diff)):
            if i < len(diff) // 2:
                res += diff[i][1] # add the cost of first city
            else:
                res += diff[i][2] # add the cost of second city
        return res