class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def get_next(i):
            # Standard circular array indexing
            return (i + nums[i]) % n

        for i in range(len(nums)):
            slow, fast = i, get_next(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[get_next(fast)] > 0:
                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True
                slow = get_next(slow)
                fast = get_next(get_next(fast))
            j = i
            while nums[j] * nums[get_next(j)] > 0:
                temp = j
                j = get_next(j)
                nums[temp] = 0
        return False