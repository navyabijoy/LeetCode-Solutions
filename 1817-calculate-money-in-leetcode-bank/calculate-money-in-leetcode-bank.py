class Solution:
    def totalMoney(self, n: int) -> int:
        days, ans = n, 0
        i = 0
        while i <= n // 7:
            k = i + 1
            if days // 7 == 0:
                for _ in range(days):
                    ans += k
                    k += 1
            else:
                for _ in range(7):
                    ans += k
                    k += 1
                days -= 7
            i += 1
        return ans