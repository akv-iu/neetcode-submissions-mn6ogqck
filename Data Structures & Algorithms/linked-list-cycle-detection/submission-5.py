# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        
        slow = head
        if not slow:
            return False
            
        elif not slow.next:
            return False
        elif not slow.next.next:
            return False


        fast = head.next.next

        while fast and fast.next:
            
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next
        
        return False
        