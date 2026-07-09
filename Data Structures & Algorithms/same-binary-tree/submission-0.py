# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.rec(p,q) == -1:
            return False
        return True
    def rec(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> int:
        if p is None and q is None:
            return 0
        if p is None or q is None:
            return -1
        if p.val != q.val:
            return -1
        left = self.rec(p.left, q.left)
        right = self.rec(p.right, q.right)
        if left == -1 or right == -1:
            return -1
        return 0