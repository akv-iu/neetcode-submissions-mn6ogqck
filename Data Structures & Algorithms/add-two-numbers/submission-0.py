# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        final = ListNode()
        curr = final
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0    

            sum = v1 + v2 + carry
            if sum >= 10:
                carry = int(sum / 10)
                print(f"carry = {carry}")
                val = sum % 10
                
            else:
                val = sum
                carry = 0
            
            ans = ListNode(val)
            curr.next = ans
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        return final.next
                

        
