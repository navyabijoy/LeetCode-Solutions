class Solution:
    def reverse(self, left, right, arr):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # to make sure its within the length of n
        self.reverse(0,n-1,nums)
        self.reverse(0,k-1,nums)
        self.reverse(k,n-1,nums)
