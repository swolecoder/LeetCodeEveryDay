# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node): 
            if not node:
                return 0,True
            
            hL,checkerL = helper(node.left)
            hR, checkerR = helper(node.right)
            
            if not checkerL or not checkerR:
                return -1, False

            if abs(hL - hR) > 1:
                return -1,  False
            

            return max(hL, hR) + 1, True
        return helper(root)[1]



        