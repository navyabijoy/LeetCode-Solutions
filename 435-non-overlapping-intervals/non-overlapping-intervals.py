class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        remove = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end # we choose minimum to minimize the removals
                
            else:
                remove += 1
                prevEnd = min(prevEnd, end)
        return remove