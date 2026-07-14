# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        temp = ans
        carry = 0
        while l1 or l2 or carry:
            s = carry 
            if l1:
                s+=l1.val
                l1 = l1.next
            if l2:
                s+=l2.val
                l2 = l2.next
            carry = int(s / 10)
            temp.next = ListNode(s % 10)
            temp = temp.next
            
    
        # if carry:
        #     temp.next = ListNode(carry)

        return ans.next
            