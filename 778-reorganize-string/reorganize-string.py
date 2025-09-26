class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = Counter(s)
        maxHeap = []
        for c,n  in hashmap.items():
            heappush(maxHeap, (-n,c))

        res = ""
        while maxHeap:
            currChar = maxHeap[0][1]
            currCount = -maxHeap[0][0]
            heappop(maxHeap)
            if len(res) >= 1 and res[-1]==currChar:
                if not maxHeap:
                    return ""
                nextChar = maxHeap[0][1]
                nextCount = -maxHeap[0][0]
                heappop(maxHeap)

                res += nextChar
                nextCount -= 1
                if nextCount > 0:
                    heappush(maxHeap, (-nextCount, nextChar))
            else:
                res += currChar
                currCount -= 1
            
            if currCount > 0:
                heappush(maxHeap, (-currCount, currChar))
        return res


