class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        left = 0
        right = len(people)-1
        while limit > 0 and left <= right:
            total = people[left] + people[right]
            if total <= limit:
                left += 1
            right -= 1
            boat += 1
        return boat