# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        endList = []
        # left first then right then finally node

        def helper(self, node):
            if node == None:
                return
            
            helper(self, node.left) 
            helper(self, node.right)
            endList.append(node.val)

        helper(self, root)

        return endList
