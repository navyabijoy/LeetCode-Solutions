class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        res = ""
        if a > 0:
            heappush(maxHeap, (-a, 'a'))
        
        if b > 0:
            heappush(maxHeap, (-b, 'b'))

        if c > 0:
            heappush(maxHeap, (-c, 'c'))

        while maxHeap:
            currChar = maxHeap[0][1]
            currCount = -maxHeap[0][0]
            heappop(maxHeap)

            if len(res) >= 2 and res[-1] == res[-2] == currChar:
                if not maxHeap:
                    break
                #the last 2 alphabets are similar, need to use next character
                nextChar = maxHeap[0][1]
                nextCount = -maxHeap[0][0]
                heappop(maxHeap)
                res += nextChar

                nextCount -= 1
                if nextCount > 0:
                    heappush(maxHeap, (-nextCount, nextChar))
            else:
                #last 2 characters are not similar, hence we can use the same character
                res += currChar
                currCount -=1 

            if currCount > 0:
                heappush(maxHeap, (-currCount, currChar))

        return res
