#uses a carry number for over 10
#accounts for different l1 and l2 sizes



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sentinel = ListNode(0)
        current = sentinel
        carry = 0
        
        while l1 is not None or l2 is not None:
            #while there are nodes left in l1 and l2 adds
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            total = carry + x + y
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            #moves pointer over for each l
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return sentinel.next
    