# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        end = None
        second = slow.next
        slow.next = None
        curr = second
        

        while curr:
            temp = curr.next
            curr.next = end
            end = curr
            curr = temp
        
        first, second = head, end

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        


