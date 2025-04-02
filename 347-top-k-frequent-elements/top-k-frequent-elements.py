class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        
        minHeap = []
        for num, freq in hashMap.items():
            heapq.heappush(minHeap, (freq,num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
                
        return [y for x,y in minHeap]