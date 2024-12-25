'''
Create TWO stacks, s1 and s2. Let x be the input value:
- Push - 
S1 -> S2
X -> S1
S2 -> S1
'''
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())


    def pop(self) -> int:
        val = self.s1.pop()
        return val
        
    def peek(self) -> int:
        return self.s1[-1]
        
    def empty(self) -> bool:
        return len(self.s1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()