# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def length(self, head):
        if not head:
            return 0
        return 1 + self.length(head.next)

    def length2(self,head):
        n = 0
        while head:
            n+=1
            head = head.next
        return n
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.length(head)
        temp = ListNode()
        ans = temp
        temp.next = head

        # t 1 2 3 4 5
        for _ in range(l-n):
            temp = temp.next

        temp.next = temp.next.next

        return ans.next
        