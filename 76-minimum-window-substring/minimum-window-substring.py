class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or s == "" or t == "":
            return "" 

        t_map = Counter(t)
        window_count = {ch:0 for ch in t_map} 
        required = len(t_map)
        formed = 0

        left = 0
        min_len = float('inf')
        res = ""
        
        for right,ch in enumerate(s):
            if ch in window_count:
                window_count[ch] += 1
                if window_count[ch] == t_map[ch]:
                    formed += 1
            
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]
                
                left_ch = s[left]
                if left_ch in window_count:
                    window_count[left_ch] -= 1
                    if window_count[left_ch] < t_map[left_ch]:
                        formed -= 1
                left += 1
        return res