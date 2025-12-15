# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        finalList = []
        levelMap = defaultdict(list)
        depth = 1

        def bfs(root, level):
            nonlocal depth
            q = deque()
            q.append((root, level))
            

            while q:
                node, lev = q.popleft()

                levelMap[lev].append(node.val)

                if node.left:
                    q.append((node.left, lev+1))
                if node.right:
                    q.append((node.right, lev+1))

                if node.right or node.left:
                    depth += 1

        bfs(root, 0)

        # iterate through levels
        for i in range(depth):
            finalList.append(levelMap[i])

        while finalList[-1] == []:
            finalList.pop()

        return finalList