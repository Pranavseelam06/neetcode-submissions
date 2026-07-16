# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        count = [-1000]
        self.dfs(root, count)
        return self.good
    def dfs(self, root: TreeNode, count: list[int]) -> None:
        if root is None:
            return
        print(root.val)
        print(count[0])
        if root.val >= count[0]:
            self.good = self.good + 1
        count.append(root.val)
        count.sort(reverse=True)
        self.dfs(root.left, count)
        self.dfs(root.right, count)
        count.remove(root.val)
        return