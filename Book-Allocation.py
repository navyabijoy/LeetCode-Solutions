from os import *
from sys import *
from collections import *
from math import *

def isPossible(noOfDays,noOfBooks,timeTaken,mid):
    
    pageSum = 0
    days = 1
    for i in range(noOfBooks):
        if pageSum + timeTaken[i] <= mid:
            pageSum += timeTaken[i]
            
        else:
            days += 1
            if days > noOfDays or timeTaken[i] > mid:
                return False
            pageSum = timeTaken[i]
            
    return True


def ayushGivesNinjatest(n, m, time):
    left = 0
    right = sum(time)
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if isPossible(n,m,time,mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
