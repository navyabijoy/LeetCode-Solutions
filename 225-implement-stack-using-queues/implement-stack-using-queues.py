class MyStack:

    def __init__(self):
        self.q = deque() # define the queue using deque()

    def push(self, x: int) -> None:
        self.q.append(x) #just append the queue in the stack
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft()) # pop all the items from the front and append them to the back of the queue so that when pop function is implemented, it returns the newly added value

    def pop(self) -> int:
        return self.q.popleft() # returns the newly added number since the queue was reversed
        

    def top(self) -> int:
        return self.q[0] #returns the first number
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()