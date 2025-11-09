class Solution:
    def reorganizeString(self, s: str) -> str:
        track = Counter(s)
        maxHeap = []
        res = []

        for ch, num in track.items():
            heapq.heappush(maxHeap, (-num,ch))

        prev = None

        while maxHeap:
            freq, ch = heapq.heappop(maxHeap)
            res.append(ch)
            freq += 1 # increase as the freq is negative
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if freq < 0:
                prev = (freq, ch)
            
        res = "".join(res)
        return res if len(res) == len(s) else ""
            
