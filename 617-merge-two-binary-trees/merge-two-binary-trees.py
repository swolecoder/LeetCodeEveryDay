# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:



        def dfs(p,q):
            if not p and not q:
                return None
            if not p:
                return q
            
            if not q:
                return p
            v1 = p.val if p.val else 0
            v2 = q.val if q.val else 0

            root = TreeNode(v1+v2)

            root.left = dfs(p.left, q.left)
            root.right = dfs(p.right, q.right)
            return root
        
        return dfs(root1,root2)

        