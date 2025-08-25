# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])

        ans = []

        while q:
            l = []
            for _ in range(len(q)):
                data = q.popleft()
                l.append(data.val)

                if data.left: q.append(data.left)
                if data.right: q.append(data.right)
            
            ans.append(l)
        return ans
        