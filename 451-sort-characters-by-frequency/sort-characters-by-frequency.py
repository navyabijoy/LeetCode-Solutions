class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        buckets = defaultdict(list)

        for char,cnt in count.items():
            buckets[cnt].append(char)
        res = []
        for i in range(len(s),0,-1):
            for c in buckets[i]:
                res.append(c*i)
        return ''.join(res)
        