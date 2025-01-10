class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for b in words2:
            freq_b = Counter(b)
            for char in freq_b:
                max_freq[char] = max(max_freq[char], freq_b[char])

        res = []
        for a in words1:
            freq_a = Counter(a)
            if all(freq_a[char] >= max_freq[char] for char in max_freq):
                res.append(a)
        
        return res