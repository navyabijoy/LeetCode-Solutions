class Solution:
    def helper(self,nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        prev2 = 0
        prev1 = nums[0]
        for i in range(1,n):
            pick =  nums[i%n] + prev2
            not_pick = prev1
            curr = max(pick, not_pick)
            prev2 = prev1
            prev1 = curr

        return prev1
    def rob(self, nums: List[int]) -> int:
        arr1 = []
        arr2 = []
        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(n):
            if i != 0:
                arr1.append(nums[i])
            if i != n - 1:
                arr2.append(nums[i])

        ans1 = self.helper(arr1)
        ans2 = self.helper(arr2)

        return max(ans1, ans2)