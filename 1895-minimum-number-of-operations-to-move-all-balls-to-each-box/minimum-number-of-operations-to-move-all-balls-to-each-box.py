class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        balls = 0
        operations = 0
        for i in range(n):
            answer[i] += operations
            balls += int(boxes[i])
            operations += balls
        balls = 0
        operations = 0
        for i in range(n-1,-1,-1):
            answer[i] += operations
            balls += int(boxes[i])
            operations += balls
        return answer

