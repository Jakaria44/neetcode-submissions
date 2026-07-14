# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.count = 0
    
    def f(self, root, maxVal):
        if not root:
            return maxVal
        
        if root.val >= maxVal:
            self.count+=1
            maxVal = root.val
        
        self.f(root.left, maxVal)
        self.f(root.right, maxVal)

    def goodNodes(self, root: TreeNode) -> int:
        self.f(root, -101)
        return self.count