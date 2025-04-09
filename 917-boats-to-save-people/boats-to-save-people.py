class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        total = 0
        count = 0
        while left <= right:
            total = people[left] + people[right]
            if total <= limit:
                left += 1
            right -= 1
            count += 1
        return count