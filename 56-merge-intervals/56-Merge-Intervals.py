class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            last_added = result[-1]
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            past_end = last_added[1]
            if curr_start <= past_end:
                result[-1][1] = max(curr_end, past_end)
            else:
                result.append([curr_start, curr_end])
        
        return result