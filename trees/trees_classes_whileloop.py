class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                if value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right
    
    def lookup(self, value):
        if self.root is None:
            return False
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return current_node
        return False
            
    def remove(self, value):
        if self.root is None:
            return False
        current_node = self.root
        parent_node = None

        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                # Option 1: No right child
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        else:
                            parent_node.right = current_node.left

                # Option 2: Right child which doesn't have a left child
                elif current_node.right.left is None:
                    current_node.right.left = current_node.left
                    if parent_node is None:
                        self.root = current_node.right
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        else:
                            parent_node.right = current_node.right

                # Option 3: Right child that has a left child
                else:
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if parent_node is None:
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        else:
                            parent_node.right = leftmost

                return True
        return False
