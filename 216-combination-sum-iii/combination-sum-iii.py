class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(start,current_sum):
            if len(sol[:]) == k:
                if current_sum == n:
                    res.append(sol[:])
                return

            for num in range(start, 10):
                if current_sum + num > n:
                    break  # No point in continuing if the sum exceeds n

                sol.append(num)
                backtrack(num + 1, current_sum + num)
                sol.pop()
            

        backtrack(1, 0)
        return res