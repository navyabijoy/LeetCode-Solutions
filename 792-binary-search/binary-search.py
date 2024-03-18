class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        f=0
        l=n-1
        while f<=l:
            mid=(f+l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                f=mid+1
            else:
                l=mid-1
        return -1
        