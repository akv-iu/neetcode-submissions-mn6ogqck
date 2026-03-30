# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode()
        dummy.next = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            
        curr = dummy
        

        count2 = 0
        while curr.next:
            print(curr.val)
            if count2 == (count-n):
                
                curr.next = curr.next.next
                count2 +=1
                
            else:
                curr = curr.next
                count2 +=1
                
        
        return(dummy.next)
        