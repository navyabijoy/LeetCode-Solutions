class Solution:
    def solve(self, nums1, nums2, i, j, dp):
        if i == len(nums1) or j == len(nums2):
            return float("-inf")

        if dp[i][j] != None:
            return dp[i][j]

        val = nums1[i] * nums2[j]
        take_i_j = max(val, val + self.solve(nums1, nums2, i + 1, j + 1, dp))
        take_i = self.solve(nums1, nums2, i, j + 1, dp)
        take_j = self.solve(nums1, nums2, i + 1, j, dp)

        dp[i][j] = max(val, take_i_j, take_i, take_j)

        return dp[i][j]

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[None] * len(nums2) for _ in range(len(nums1))]

        return self.solve(nums1, nums2, 0, 0, dp)
