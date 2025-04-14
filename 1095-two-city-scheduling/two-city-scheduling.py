class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_cost = 0
        costs.sort(key = lambda x:x[0]-x[1])
        costs_length = len(costs)
        for i in range(costs_length//2):
            total_cost = total_cost + costs[costs_length-i-1][1] + costs[i][0]
        return total_cost