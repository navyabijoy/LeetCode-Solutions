class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = intervals + [newInterval]
        newIntervals.sort(key= lambda i: i[0])
        output=[newIntervals[0]]
        for start,end in newIntervals[1:]:
            
            lastEnd = output[-1][1]
            if lastEnd >= start:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
        return output
        