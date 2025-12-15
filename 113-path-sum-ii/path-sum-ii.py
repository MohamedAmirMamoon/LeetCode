# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # root to leaf path == target
        sumFound = False
        finalList = []
        tempList = []

        def dfs(node, sumTracker):
            nonlocal sumFound
            nonlocal tempList
            nonlocal finalList
            if not node:
                return

            sumTracker += node.val
            tempList.append(node.val)

            if not node.left and not node.right:
                if targetSum == sumTracker:
                    sumFound = True
                    print(tempList)
                    finalList.append(tempList.copy())
            
            dfs(node.left, sumTracker)
            dfs(node.right, sumTracker)
            tempList.pop()


        dfs(root, 0)

        return finalList
        