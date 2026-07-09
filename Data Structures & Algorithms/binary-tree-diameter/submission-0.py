# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.value = 0
        self.defrec(root)
        return self.value
        
    def defrec(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.defrec(root.left)
        right = self.defrec(root.right)
        self.value = max(self.value, left + right)
        return 1 + max(left,right)
