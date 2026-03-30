# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        res = []
        ans = self.small(root,res)
        return ans[k-1]
    
    def small(self, root, res):
        if not root:
            return 
        self.small(root.left,res)
        res.append(root.val)
        self.small(root.right,res)
        return res

            
        
        