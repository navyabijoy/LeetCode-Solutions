class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        '''
        Time Complexity: O(n * k)
        Space Complexity: O(n - k + 1)
        '''
        def ifSorted(nums):
            '''
            Helper function to check if the given sub_arr is consecutive and sorted or not
            '''
            for i in range(len(nums)-1):
                if nums[i+1] != (nums[i] + 1): 
                    return False
            return True

        result = [-1] * (len(nums) - k + 1)
        for i in range(len(nums) - k + 1):
            j = (i + k - 1)
            sub_arr = nums[i:j+1]
            # Checking the given constraint for the every possible sub_arr of size (i + k -1)
            if ifSorted(sub_arr) and len(sub_arr) == len(set(sub_arr)):
                result[i] = max(sub_arr)

        return result