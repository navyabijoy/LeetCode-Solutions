class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l, r = 0,0
        count = 0
        g.sort()
        s.sort()
        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                l += 1
                count += 1
            r += 1
        return count
