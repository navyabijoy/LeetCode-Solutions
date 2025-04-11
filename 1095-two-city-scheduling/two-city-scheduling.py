class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_cost = 0
        costs.sort(key = lambda x : x[0] - x[1])
        cost_length = len(costs)
        for i in range(cost_length//2):
            total_cost = total_cost + costs[i][0] + costs[cost_length-i-1][1]
        return total_cost