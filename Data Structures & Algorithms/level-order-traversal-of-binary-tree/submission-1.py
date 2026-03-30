# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.level(root, res, 0)
        return res

    def level(self, root, res, level):
        if not root:
            return
        
        if len(res) == level:
            res.append([])
        
        res[level].append(root.val)
        self.level(root.left, res, level + 1)
        self.level(root.right, res, level + 1)
        