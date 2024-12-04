class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        sorted_chars = [char * freq for char, freq in sorted(count.items(), key=lambda x: x[1], reverse=True)]
        return ''.join(sorted_chars)
        