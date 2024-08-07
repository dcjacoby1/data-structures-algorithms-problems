# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#head increments by 1, fast by 2
# if head and fast colide, means theres a cycle, otherwise there isn't
def hasCycle(head):
        fast = head
        while(fast and fast.next):
            head = head.next
            fast = fast.next.next
            if head == fast:
                return True          
        return False

#time complexity
#O(n) for number of links in LinkedList

#space complexity
# uses 2 pointers, O(1)
