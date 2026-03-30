# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        new = deque()
        new.append(root)
        res = []
        eachres = []

        while new:
            level = []
            for i in range(len(new)):
                node = new.popleft()
                if node:
                    level.append(node.val)
                    new.append(node.left)
                    new.append(node.right)

            if len(level) != 0:
                res.append(level)
        
        return res
            
        