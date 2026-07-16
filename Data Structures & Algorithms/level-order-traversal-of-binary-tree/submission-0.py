# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.lists = {}
        if root is None:
            return []
        self.dfs(root, 1)
        return list(self.lists.values())
    def dfs(self, root: Optional[TreeNode], depth: int) -> None:
        if root is None:
            return
        if depth not in self.lists:
            self.lists[depth] = []
        self.lists[depth].append(root.val)
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
        return