# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # return all root to leaf paths in any order

        finalOrder = []
        def dfs(root, path):
            if not root:
                return None

            if path:
                path = path + '->' + str(root.val)
            else:
                path = str(root.val)
            

            dfs(root.left, path)
            dfs(root.right, path)

            if not root.left and not root.right:
                # then leaf node
                finalOrder.append(path)

        dfs(root, "")

        return finalOrder
        