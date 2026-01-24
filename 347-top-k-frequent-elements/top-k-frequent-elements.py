class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = Counter(nums)
        maxHeap = []
        for num, count in track.items():
            heapq.heappush(maxHeap, (-count, num))

        res = []
        while k:
            cnt, n = heapq.heappop(maxHeap)
            res.append(n)
            k -= 1
        return res