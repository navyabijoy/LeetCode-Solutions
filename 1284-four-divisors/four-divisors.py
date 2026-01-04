class Solution:
    def findDivisors(self, n):
        res = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
            i += 1
        return res

    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            ans = self.findDivisors(num)
            if len(ans) == 4:
                total += sum(ans)
        return total