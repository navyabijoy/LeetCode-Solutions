class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        container_max =  0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            curr = width * h

            container_max = max(container_max, curr)
            
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return container_max

