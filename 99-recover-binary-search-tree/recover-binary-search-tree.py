# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
    
        inOrder = []

        def dfs(node):
            nonlocal inOrder
            if not node:
                return


            dfs(node.left)
            inOrder.append(node)
            dfs(node.right)

        dfs(root)  
            
            
        sortedOrder = [node.val for node in inOrder]
        sortedOrder.sort()

        for i in range(len(sortedOrder)):
            inOrder[i].val = sortedOrder[i]
            

              


        