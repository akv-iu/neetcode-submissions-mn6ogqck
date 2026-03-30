# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checking(root, -1001, 1001)

    def checking(self,root, lower, upper):
        if not root:
            return True
        if not lower < root.val or not root.val < upper:
            return False
        
        return (self.checking(root.left, lower, root.val) and 
        (self.checking(root.right,root.val,upper)))
            


        
        