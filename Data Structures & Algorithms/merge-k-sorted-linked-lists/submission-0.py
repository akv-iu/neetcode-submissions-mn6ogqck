# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(first,second):
            dummy = ListNode()
            curr = dummy
            
            while second is not None:
                if first is None:
                    dummy.next = second
                    return curr.next
                if first.val <= second.val:
                    dummy.next = first
                    first = first.next
                    dummy = dummy.next
                
                else:
                    dummy.next = second
                    second = second.next
                    dummy = dummy.next
            
            dummy.next = first
            return curr.next
    
        while len(lists) > 1:
            
            lists.append(merge(lists.pop(),lists.pop()))
        if lists:
            return lists[0]
        return 





        