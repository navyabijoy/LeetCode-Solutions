class Solution:
    def NSE(self, arr):
        st = []
        ans = [len(arr)] * len(arr)
        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            ans[i] = st[-1] if st else len(arr)
            st.append(i)
        return ans

    def PSE(self, arr):
        st = []
        ans = [-1] * len(arr)
        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans
    
    def NGE(self, arr):
        st = []
        ans = [len(arr)] * len(arr)
        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]] < arr[i]:
                st.pop()
            ans[i] = st[-1] if st else len(arr)
            st.append(i)
        return ans
    
    def PGE(self, arr):
        st = []
        ans = [-1] * len(arr)
        for i in range(len(arr)):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans

    def subArrayRanges(self, nums: List[int]) -> int:
        nse = self.NSE(nums)
        pse = self.PSE(nums)
        nge = self.NGE(nums)
        pge = self.PGE(nums)
        total = 0
        for i in range(len(nums)):
            leftMin = i - pse[i]
            rightMin = nse[i] - i
            leftMax = i - pge[i]
            rightMax = nge[i] - i
            freqMin = leftMin * rightMin
            freqMax = leftMax * rightMax
            total = total + ((freqMax * nums[i]) - (freqMin * nums[i]))
        return total
