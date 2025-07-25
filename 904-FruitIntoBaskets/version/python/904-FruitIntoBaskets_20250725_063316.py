# Last updated: 7/25/2025, 6:33:16 AM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)
        collected = 0
        left = 0
        for right in range(len(fruits)):
            baskets[fruits[right]] += 1
            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
            collected = max(collected, right - left + 1)
        return collected


            