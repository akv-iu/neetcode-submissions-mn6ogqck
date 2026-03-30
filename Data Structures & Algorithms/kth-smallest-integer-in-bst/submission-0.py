class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        r = [0]  # shared counter
        
        def inorder(root, k, r):
            if not root:
                return None
            
            # Recurse left
            left = inorder(root.left, k, r)
            if left is not None:
                return left  # propagate found value
            
            # Visit current node
            r[0] += 1
            if r[0] == k:
                return root.val  # found kth smallest
            
            # Recurse right
            return inorder(root.right, k, r)
        
        return inorder(root, k, r)