# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

#time limit exceeded bc of dictionary
class Solution1(object):
    def detectCycle(self, head):
        node_dict = {}
        current = head
        while (current and current.next):
            if current.next in node_dict:
                return current.next
            else:
                node_dict[current] = True
                current = current.next
        return None
    
#O(N) for time and space



#better solution
class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        # Phase 1: Detect if there is a cycle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected
                break
        else:
            # No cycle detected
            return None

        # Phase 2: Find the start of the cycle
        pointer1 = head
        pointer2 = slow
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        return pointer1
         #this part works bc the point they meet will always be the same amount
         #of steps as the distance from head to entry point of cycle
         #floyds tortoise and hare proves this
         #time O(n) space O(1)

   