# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x):
        if not self.s1:
            self.front = x
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        self.front = self.s1[-1]
        

    def pop(self):
        if self.s1:
            popped = self.s1.pop()
            if self.s1:
                self.front = self.s1[-1]
            else:
                self.front = None 
            return popped
        return None

        

    def peek(self):
        return self.front if self.s1 else None
        

    def empty(self):
        return not self.s1