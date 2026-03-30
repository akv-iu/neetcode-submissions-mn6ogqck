
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, had: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        end = None

        if not curr:
            return curr


        while curr.next:
            temp = curr.next
            curr.next = end
            end = curr
            curr = temp
        
        curr.next = end
        return(curr)