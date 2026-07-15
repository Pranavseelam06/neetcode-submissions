# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None
        self.rec_DFS(root, p, q)
        return self.ans

    def rec_DFS(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Set:
        if root is None:
            return set()
        empty_set = set()
        empty_set.update(self.rec_DFS(root.left,p,q))
        empty_set.update(self.rec_DFS(root.right,p,q))
        empty_set.add(root.val)
        if p.val in empty_set and q.val in empty_set:
            if self.ans is None:
                self.ans = root
        return empty_set
