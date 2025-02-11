class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        result.append(intervals[0]) # append the first interval
        for i in range(1,len(intervals)):
            curr_start,curr_end = intervals[i]
            last_interval = result[-1]
            prev_end = last_interval[1]
            
            if curr_start <= prev_end:
                result.pop()
                result.append([last_interval[0],max(curr_end,prev_end)])
            else:
                result.append(intervals[i])
        return result