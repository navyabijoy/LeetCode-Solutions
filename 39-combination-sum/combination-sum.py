class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(index, res, total):
            if total == target:
                ans.append(res[:])
                return 

            if index == len(candidates) or total > target:
                return
            
            res.append(candidates[index])
            backtrack(index, res, total + candidates[index])
            res.pop()

            backtrack(index+1, res, total)
                
        
        backtrack(0, [], 0)
        return ans