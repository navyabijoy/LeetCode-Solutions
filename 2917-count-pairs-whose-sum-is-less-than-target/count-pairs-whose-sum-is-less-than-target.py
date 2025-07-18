class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i != j and nums[i] + nums[j] < target:
                    count += 1
                    # res.append([nums[i],nums[j]])

        return count