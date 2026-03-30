# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        c1,c2 = list1,list2
        dummy2 = dummy
        

        while c1 and c2:

                
            if c1.val<=c2.val:
                dummy.next = c1
                dummy = c1
                c1 = c1.next
            else:
                dummy.next = c2
                dummy = c2
                c2=c2.next
        
        if not c1:
            dummy.next = c2
            return(dummy2.next)
        else:
            dummy.next = c1
            return(dummy2.next)
        
        







            

        