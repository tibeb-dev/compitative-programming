class MyQueue(object):

    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, x) :
        self.l1.append(x)

    def pop(self) :
        if not self.l2:
            while self.l1:
                self.l2.append(self.l1.pop())
        return self.l2.pop()    
        
    def peek(self) :
        if not self.l2:
            while self.l1:
                self.l2.append(self.l1.pop())
        return self.l2[-1] 

    def empty(self) :
        return len(self.l1) == 0 and len(self.l2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()