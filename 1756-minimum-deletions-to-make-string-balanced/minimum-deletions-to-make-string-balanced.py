class Solution:
    def minimumDeletions(self, s: str) -> int:
        num_b = 0
        min_del = 0
        for c in s:
            if c == 'a':
                min_del = min(num_b, min_del+1)
            else:
                num_b += 1
        return min_del