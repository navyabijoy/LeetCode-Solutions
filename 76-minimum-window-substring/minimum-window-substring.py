class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen = float('inf')
        minChar = ""
        t_count = Counter(t)
        window_count = Counter()

        left = 0
        for right in range(len(s)):
            window_count[s[right]] +=1 
            while all(window_count[char] >= t_count[char] for char in t_count):
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    minChar = s[left:right+1]

                window_count[s[left]] -= 1
                left += 1
            right += 1
        return minChar

