class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = Counter(nums)
        minHeap = []

        for num, freq in track.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        for freq, num in minHeap:
            res.append(num)
        return res
