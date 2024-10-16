class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for i in asteroids:
            while result and i < 0 and result[-1] > 0:
                diff = i + result[-1]
                if diff < 0:
                    result.pop()
                elif diff > 0:
                    i = 0
                else:
                    i = 0
                    result.pop()
            if i != 0:
                result.append(i)
        return result

