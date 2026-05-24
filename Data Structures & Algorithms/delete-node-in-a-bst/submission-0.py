# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # need the minimum of the tree
        def minNodeVal(root):
            current = root
            while current and current.left:
                current = current.left
            return current
        
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # found the node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = minNodeVal(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
            
        return root