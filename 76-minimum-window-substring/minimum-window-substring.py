class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        target_count = Counter(t)  # Count of characters in t
        window_count = Counter()
        
        left = 0
        right = 0
        min_len = float('inf')
        min_window = ""

        while right < len(s):
            window_count[s[right]] += 1  # Expand the window by including s[right]
            
            while all(window_count[char] >= target_count[char] for char in target_count):
                # Contract the window from left
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]
                
                window_count[s[left]] -= 1
                left += 1  # Reduce the window from the left

            right += 1  # Expand the window from the right
        
        return min_window
