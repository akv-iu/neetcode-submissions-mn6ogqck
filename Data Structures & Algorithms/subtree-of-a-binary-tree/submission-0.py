# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sametree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    def sametree(self, main, sub):
        if not main and not sub:
            return True
        if not main or not sub:
            return False
        if main.val == sub.val:
            return (self.sametree(main.left,sub.left) and self.sametree(main.right,sub.right))
        else:
            return False
        
        