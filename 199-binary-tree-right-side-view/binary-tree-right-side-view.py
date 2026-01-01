# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # so we have to track depth
        # do bfs
        # so we go level by level
        # for height of the tree, each level we would take the right most node
        inorder = []
        # add root
        # if at that node theres a left and right, we take right
        # if no right, and left take left
        q = deque()
        q.append((root, 0))
        while q:
            node, depth = q.popleft()
            if not node:
                continue
            
            # check if that depth has been put down
            if depth == len(inorder):
                inorder.append(node.val)

            left = node.left
            right = node.right
            # now we append both with their depth
            # as we go, we append right elements first
            if right:
                q.append((right, depth+1))
            if left:
                q.append((left, depth+1))
        
        return inorder
