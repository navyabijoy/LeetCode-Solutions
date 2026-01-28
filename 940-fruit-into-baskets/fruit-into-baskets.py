class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = {}
        left = 0
        maxLen = 0
        for right in range(len(fruits)):
            if fruits[right] in seen:
                seen[fruits[right]] += 1
            else:
                seen[fruits[right]] = 1

            while len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)
            
        return maxLen