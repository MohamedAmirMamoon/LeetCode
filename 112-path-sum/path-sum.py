# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # root to leaf path == target
        sumFound = False

        def dfs(node, sumTracker):
            nonlocal sumFound
            if not node:
                return

            sumTracker += node.val
            
            dfs(node.left, sumTracker)
            dfs(node.right, sumTracker)


            if not node.left and not node.right:
                if targetSum == sumTracker:
                    sumFound = True
                    

        dfs(root, 0)

        return sumFound
        