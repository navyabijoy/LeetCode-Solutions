class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack = sandwiches[::-1]
        q = deque(students)

        turn = 0 
        while q and turn < len(q):
            if q[0] == stack[-1]:
                q.popleft()
                stack.pop()
                turn = 0
            else:
                q.append(q.popleft())
                turn += 1
               
        return len(q)