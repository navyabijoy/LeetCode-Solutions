class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        intervals.sort()
        result = []
        
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            last_added_interval = result[-1]
            cur_start = intervals[i][0]
            curr_end = intervals[i][1]

            prev_end = last_added_interval[1] # accesses the second value of the last added interval

            if cur_start <= prev_end:
                result[-1][1] = max(curr_end, prev_end)
            else:
                result.append([cur_start, curr_end])
        return result
