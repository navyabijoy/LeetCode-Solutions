class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = intervals + [newInterval] #add the new interval to the list of the prev ones
        newIntervals.sort(key= lambda i: i[0]) #sort the intervals based on the numbers at the 0th index
        output=[newIntervals[0]] #output array will include the first interval beforehand
        for start,end in newIntervals[1:]: #traverse through the array
            lastEnd = output[-1][1] #last end refers to the number at the 1st index of the first interval
            if lastEnd >= start: 
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
        return output
        
