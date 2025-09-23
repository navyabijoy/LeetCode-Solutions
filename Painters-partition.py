# Problem statement
# Given an array/list of length ‘n’, where the array/list represents the boards and each element of the given array/list represents the length of each board. 
# Some ‘k’ numbers of painters are available to paint these boards. Consider that each unit of a board takes 1 unit of time to paint.
# You are supposed to return the area of the minimum time to get this job done of painting all the ‘n’ boards under a constraint that any painter will only paint the continuous sections of boards.

# Example :
# Input: arr = [2, 1, 5, 6, 2, 3], k = 2

# Output: 11

# Explanation:
# First painter can paint boards 1 to 3 in 8 units of time and the second painter can paint boards 4-6 in 11 units of time. 
#Thus both painters will paint all the boards in max(8,11) = 11 units of time. It can be shown that all the boards can't be painted in less than 11 units of time.

def findLargestMinDistance(boards:list, k:int):
    left = 0
    right = sum(boards)
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if isPossible(boards,k,mid):
            ans = mid 
            right = mid - 1
        else:
            left = mid + 1
    return ans

def isPossible(boards,k,mid):
    total = 0
    painters = 1
    for i in range(len(boards)):
        if total + boards[i] <= mid:
            total += boards[i]
        else:
            painters += 1
            if painters > k or boards[i] > mid:
                return False 
            total = boards[i]
    return True






