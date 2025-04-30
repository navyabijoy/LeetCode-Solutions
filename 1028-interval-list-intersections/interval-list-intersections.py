class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        p1 = 0
        p2 = 0
        while p1 < len(firstList) and p2 < len(secondList):
            a1,b1 = firstList[p1]
            a2,b2 = secondList[p2]
            maxStart = max(a1,a2)
            minLate = min(b1,b2)
            if maxStart <= minLate:
                result.append([maxStart, minLate])
            if minLate == b1:
                p1 += 1
            else:
                p2 += 1
        return result


