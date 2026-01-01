# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # min difference between two nodes

        # as we go throguh level by level we keep track of min diff

        # in order traversal
        minDiff = float('inf')
        previous = None

        def dfs(node):
            nonlocal minDiff, previous
            if not node:
                return
                
            dfs(node.left)
            if previous:
                minDiff = min(abs(previous.val - node.val), minDiff)
            previous = node

            dfs(node.right)

        dfs(root)
        return minDiff
