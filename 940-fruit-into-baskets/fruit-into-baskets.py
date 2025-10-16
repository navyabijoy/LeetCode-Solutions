class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        tree = defaultdict()
        left = 0
        maxLen = 0
        for right in range(len(fruits)):
            if fruits[right] in tree:
                tree[fruits[right]] += 1
            else:
                tree[fruits[right]] = 1

            while len(tree) > 2:
                tree[fruits[left]] -= 1
                if tree[fruits[left]] == 0:
                    del tree[fruits[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)
        return maxLen
            
