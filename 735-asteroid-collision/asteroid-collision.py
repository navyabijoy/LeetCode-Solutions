class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        for i in range(n):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] < abs(asteroids[i]):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        return stack

