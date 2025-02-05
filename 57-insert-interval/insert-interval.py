class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        
        result = []
        intervals.append(newInterval)
        intervals.sort()
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            last_added_interval = result[-1]

            curr_start, curr_end = intervals[i]
            prev_end = last_added_interval[1]
            if curr_start <= prev_end:
                result[-1][1] = max(curr_end, prev_end)
            else:
                result.append([curr_start, curr_end])
        return result