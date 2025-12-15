# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # min depth

        # we check eac side
        # keep track of lowest depth until node == None
        if not root:
            return 0

        depthAmount = float('inf')

        def dfs(node, depthNodes):
            nonlocal depthAmount
            if not node:
                return
            
            dfs(node.left, depthNodes+1)
            dfs(node.right, depthNodes+1)

            # once we get here donezo
            if not node.left and not node.right:
                depthAmount = min(depthNodes, depthAmount)
            return

        dfs(root, 1)

        return depthAmount



        