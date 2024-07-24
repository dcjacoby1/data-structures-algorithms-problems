# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
# Return the linked list sorted as well.

#singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#code uses 2 pointers: pred which tracks current node, head which is looking for pred.next
class Solution(object):
    def deleteDuplicates(self, head):
        # sentinel creates node before head to combat edge cases of empty nodes
        sentinel = ListNode(0, head)

        # predecessor = the last node
        # before the sublist of duplicates
        pred = sentinel

        while head:
            # If it's the beginning of a duplicates sublist
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next

                # Skip all duplicates
                pred.next = head.next

            # Otherwise, move predecessor
            else:
                pred = pred.next

            # move forward
            head = head.next  
        #returns the list starting with the first node (one after the gummy first node)
        return sentinel.next 
    
    #time is O(n) - traverses through
    #space is O(1) - only space for pointers, doesnt use any data outside data structures