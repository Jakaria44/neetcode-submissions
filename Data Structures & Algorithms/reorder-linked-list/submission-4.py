# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if not head or not head.next :
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead


    # 1 2 3 4 
    def findMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next :
            return 

        mid = self.findMid(head)
        rev = self.reverseList(mid.next)
        mid.next = None
        # merge head with rev

        # 1 2 3
        # 5 4
        fwd = head
        while rev:
            nextf = fwd.next
            nextr = rev.next

            fwd.next = rev
            rev.next = nextf

            fwd = nextf
            rev = nextr















