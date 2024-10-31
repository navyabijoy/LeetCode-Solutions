class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        res = []
        deq = deque()  # This will hold the indices of elements

        for i in range(len(nums)):
            # Remove elements out of this window
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove smaller elements as they are not useful
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            # Start adding results to res after the first k elements
            if i >= k - 1:
                res.append(nums[deq[0]])

        return res
