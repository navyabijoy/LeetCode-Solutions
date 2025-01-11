class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq_map = {}
        single_count = 0

        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1

        for freq in freq_map.values():
            if freq % 2 == 1:
                single_count += 1

        return single_count <= k and k <= len(s)