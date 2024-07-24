#under the hood for linkedLists:
#can use collections library for deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            #saves the top as pointer, so when it gets replaced, we can set it as next
            pointer = self.top
            self.top = new_node
            self.top.next = pointer

        self.length += 1
        return self

    def pop(self):
        if not self.top:
            return None
        #need this for 1 left because bottom will never get removed when one left without it
        if self.top == self.bottom:
            self.bottom = None
        pointer = self.top
        self.top = self.top.next
        self.length -= 1
        return pointer
        

#using arrays
class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        if self.array:
            return self.array[-1]
        return None

    def push(self, value):
        self.array.append(value)
        return self

    def pop(self):
        if self.array:
            self.array.pop()
        return self
    