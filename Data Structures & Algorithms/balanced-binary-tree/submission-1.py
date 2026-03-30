# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        flag = 1
        def dfs(node):
            if not node:
                return 0

                      
            if flag == 1:
            
                left = dfs(node.left)
                right = dfs(node.right)
                if left == -1 or right == -1:
                    return -1
                if not (left - right == 1 or left - right == -1 or left == right):
                    return -1
                return 1 + max(left,right)
            
            return True
        

        

       
        if dfs(root) == -1:
             return False 
        else: return True
            


        