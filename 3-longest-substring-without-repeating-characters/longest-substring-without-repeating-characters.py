class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        if len(str) == 0:
            return 0
        maxans = float("-inf")
        setx = set()
        l = 0
        for r in range(len(str)):  # outer loop for traversing the string
            if str[r] in setx:  # if duplicate element is found
                while l < r and str[r] in setx:
                    setx.remove(str[l])
                    l += 1
            setx.add(str[r])
            maxans = max(maxans, r - l + 1)
        return maxans
