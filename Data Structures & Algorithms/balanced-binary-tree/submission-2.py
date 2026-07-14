# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def get_height_imbalance(self, root):
        if not root:
            return 0

        left_h = self.get_height_imbalance(root.left)
        right_h = self.get_height_imbalance(root.right)

        if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1: 
            return -1
        
        return 1 + max(left_h, right_h)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height_imbalance(root) != -1
        