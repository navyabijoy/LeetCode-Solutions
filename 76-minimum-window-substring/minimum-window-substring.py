class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        min_len = float('inf')
        min_char = ""
        t_count = Counter(t)
        window_count = Counter()
        left = 0
        for right in range(len(s)):
            window_count[s[right]] += 1
            while all(window_count[char] >= t_count[char] for char in t_count):
                if min_len > right-left+1:
                    min_len = right - left + 1
                    min_char = s[left:right+1]
                window_count[s[left]] -= 1
                left += 1
            right += 1
        return min_char
            