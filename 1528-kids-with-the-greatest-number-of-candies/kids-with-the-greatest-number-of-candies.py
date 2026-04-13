class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        res = []
        for c in candies:
            if (c + extraCandies) >= greatest:
                res.append(True)
            else:
                res.append(False)
        return res