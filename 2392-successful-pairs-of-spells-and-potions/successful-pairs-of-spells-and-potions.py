class Solution:
    def binarySearch(self, potions,spell, success):
        low = 0
        high = len(potions) - 1
        idx = -1
        while low <= high:
            mid = (low + high) // 2
            
            if potions[mid] * spell >= success:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1
        return idx

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        m = len(potions)

        for spell in spells:
            idx = self.binarySearch(potions, spell, success)
            ans.append(m-idx if idx != -1 else 0)
        return ans
