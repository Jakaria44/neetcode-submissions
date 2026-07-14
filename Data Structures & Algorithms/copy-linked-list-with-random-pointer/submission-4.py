"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        mp = {}


        temp = head
        while temp:
            mp[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            if temp.next:
                mp[temp].next =   mp[temp.next] 
            if temp.random:
                mp[temp].random = mp[temp.random]

            temp = temp.next

        return mp[head] 