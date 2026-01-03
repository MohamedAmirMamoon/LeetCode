class MyQueue:
    # first in first out
    # 1 3 5 2 12
    # added in all negative format?

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        # how do we pop the beginning element of array or stack?
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return False if self.stack else True



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()