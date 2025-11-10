class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(index, temp):
            if index == len(nums):
                answer.append(temp[:])
                return
            
            # we include the number
            temp.append(nums[index])
            backtrack(index + 1, temp)
            temp.pop()
            
            # we skip the number
            backtrack(index+1, temp)
        
        backtrack(0,[])
        return answer