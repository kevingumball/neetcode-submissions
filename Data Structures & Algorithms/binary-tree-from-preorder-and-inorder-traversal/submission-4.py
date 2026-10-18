# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            node = TreeNode()
            node.val = preorder[self.pre_idx]
            self.pre_idx += 1
            idx = indices[node.val]
            node.left = dfs(l, idx-1)
            node.right = dfs(idx+1, r)
            return node

        return dfs(0, len(preorder) - 1)
        