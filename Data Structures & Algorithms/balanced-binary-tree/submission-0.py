# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        count = self.dfs(root)
        if count == -1:
            return False
        return True

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if right == -1 or left == -1:
            return -1
        if left > right + 1:
            return -1
        if right > left + 1:
            return -1
        return 1 + max(left,right)