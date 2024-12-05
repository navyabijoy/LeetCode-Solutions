class Solution:
    def maxDepth(self, s: str) -> int:
        count= 0
        max_count = 0
        for bracket in s:
            if bracket == "(":
                count += 1
                max_count = max(max_count, count)

            elif bracket == ")":
                count -= 1
                
        return max_count
