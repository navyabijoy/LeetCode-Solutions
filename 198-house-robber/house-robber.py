class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        one = nums[0]
        two = 0
        for i in range(1, n):
            pick = nums[i]
            if ( i > 1):
                pick += two
            notPick = 0 + one
            curr = max(pick, notPick)
            two = one
            one = curr
        return one
