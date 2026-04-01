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
            mergeans = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergeans.append(merge(l1,l2))
            lists = mergeans
            
            
        if lists:
            return lists[0]
        return 





        