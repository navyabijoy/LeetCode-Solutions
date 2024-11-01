class Solution:

    def __init__(self, weights):
        self.running_sums = []
        running_sum = 0

        for w in weights:
            running_sum += w
            self.running_sums.append(running_sum)
        
        self.total_sum = running_sum

    # Method to pick an index based on the weights
    def pickIndex(self):
        target = random.randint(1, self.total_sum)
        low = 0
        high = len(self.running_sums)

        while low < high:
            mid = low + (high - low) // 2
            if target > self.running_sums[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()