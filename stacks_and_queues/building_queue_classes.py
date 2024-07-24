#same as the stack, except the enqueue adds to the end instead of the beginning of the line

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first  = new_node
            self.last = new_node
        else:
            #makes the last node equal to the new node and then adds the new node after as the new last node
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        if not self.first:
            return None
        #if theres one node in the list (self.last is not the same as self.next)
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return self
