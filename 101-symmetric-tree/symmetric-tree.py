# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # check if it is symmetric from root

        # should be inverted

        def dfs(left, right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            
            return (left.val == right.val
                    and dfs(left.left, right.right) 
                    and dfs(left.right, right.left))
                    
        return dfs(root.left, root.right)
