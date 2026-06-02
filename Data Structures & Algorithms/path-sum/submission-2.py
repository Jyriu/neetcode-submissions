# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currentSum = 0
        
        def sumTrack(node, currentSum):
            if not node:
                return False
            
            currentSum += node.val

            if (not node.left and not node.right) and (currentSum == targetSum):
                return True
            
            if sumTrack(node.left, currentSum):
                return True

            if sumTrack(node.right, currentSum):
                return True
            
            # currentSum -= node.val
            return False

        return sumTrack(root, currentSum)