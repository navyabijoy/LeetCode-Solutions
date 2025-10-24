class Solution:
    def NSE(self, arr):
        n = len(arr)
        stack = []
        ans = [0] * n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else n
            stack.append(i)
        return ans
    
    def PSE(self, arr):
        n = len(arr)
        stack = []
        ans = [0] * n
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(i) # add index as we need the range in index
        return ans


    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse = self.NSE(arr)
        pse = self.PSE(arr)

        n = len(arr)
        total = 0
        MOD = 10**9 + 7
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            freq = left * right
            total = (total + freq * arr[i]) % MOD
        return total
        
        
        