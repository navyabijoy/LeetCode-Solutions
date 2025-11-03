class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_time = neededTime[0]
        total = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                total += min(prev_time, neededTime[i])
                prev_time = max(prev_time, neededTime[i])
            else:
                prev_time = neededTime[i]
        return total