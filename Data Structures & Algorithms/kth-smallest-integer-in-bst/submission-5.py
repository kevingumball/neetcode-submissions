# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = 0
        value = None

        def dfs(node):
            nonlocal cur
            nonlocal k
            nonlocal value
            if not node:
                return 
            dfs(node.left)
            cur += 1
            if cur == k:
                value = node.val
                return
            dfs(node.right)

        dfs(root)
        return value
        