class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = list()

        def inorder(root):
            if not root:
                return
            
            left = inorder(root.left)
            res.append(root.val)
            right = inorder(root.right)
        
        inorder(root)
        return res[k-1]