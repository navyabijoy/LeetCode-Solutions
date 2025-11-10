class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        res = []
        def backtrack(start, total ):
            if len(res[:]) == k:
                if total == n:
                    ans.append(res[:])
                return
            
            for num in range(start, 10):
                if total + num > n:
                    break
                res.append(num)
                backtrack(num+1, total + num)
                res.pop()

        
        backtrack(1,0)
        return ans