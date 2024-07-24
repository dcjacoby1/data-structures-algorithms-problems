# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


#LL is already sorted, so dont need to sort at the end
#we can assume there is no cycle in the LL, bc there is a head and sorted. cant be sorted if loops around

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        #while condition checks if there is a first value and next value
        while (current and current.next):
            #if the current value is equal to next, remove
            if current.next.val == current.val:
                current.next = current.next.next
            #otherwise, move to the next
            else:
                current = current.next
        return head

