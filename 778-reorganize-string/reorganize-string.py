class Solution:
    def reorganizeString(self, s: str) -> str:
        hashMap = Counter(s)
        maxHeap = []
        res = []
        for char,freq in hashMap.items():
            heapq.heappush(maxHeap, (-freq,char))

        prev_char, prev_count = "",0
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            res.append(char)
            if prev_count < 0:
                heapq.heappush(maxHeap,(prev_count, prev_char))
            prev_count, prev_char = count + 1, char
        return "".join(res) if len(res) == len(s) else ""
            
                 