class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or k == i:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0 and num >= 100:
                        res.add(num)
        final = sorted(list(res))
        return final