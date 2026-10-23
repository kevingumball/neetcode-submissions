# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        cur = []
        def dfs(node):
            if not node:
                cur.append("N")
                return 
            cur.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        res = ",".join(map(str, cur))
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        cur = data.split(",")
        self.idx = 0
        
        def dfs():
            if cur[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(int(cur[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()



        
