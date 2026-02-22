class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = defaultdict(list)
        maxLen = 0
        left = 0
        for right in range(len(fruits)):
            if fruits[right] in types:
                types[fruits[right]] += 1
            else:
                types[fruits[right]] = 1

            while len(types) > 2:
                types[fruits[left]] -= 1
                if types[fruits[left]] == 0:
                    del types[fruits[left]] 
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen

            