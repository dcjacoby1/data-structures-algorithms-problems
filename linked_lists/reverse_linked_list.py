#reverse a linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

#ex: 1 -> 2 -> 3 -> None
#first iteration
#next temp = 2
#1.next = None
#prev = 1
#curr = 2
#Output: prev = 1 -> None, curr = 2, 3 -> None

#second iteration
#next temp = 3
#2.next = 1
#prev = 2
#curr = 3
#Output: prev = 2 -> 1 -> None, curr = 3 -> None

#third iteration
#next temp = None
#3.next = 2
#prev = 3
# curr = None
#Output: prev = 3-> 2 -> 1 -> None, curr =  None
#cycle stops


#time = O(n) traverses throught
#space = O(1) only uses pointers, no outside data structures


