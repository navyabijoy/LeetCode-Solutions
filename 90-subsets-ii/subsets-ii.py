class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(i, res):
            if i == len(nums):
                if res not in ans:
                    ans.append(res.copy())
                return

            res.append(nums[i])
            backtrack(i+1,res)
            res.pop()

            backtrack(i+1,res)
        backtrack(0,[])
        return ans