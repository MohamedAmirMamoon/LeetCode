"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # post order traversal
        # left right finally cetner
        postOrder = []

        # we input root
        # we go as far left as possible, add
        # we go right add
        # then we add node afterwards
        if not root:
            return []

        def dfs(node):
            if not node:
                return
            
            for child in node.children:
                dfs(child)
                print(child.val)
                postOrder.append(child.val)
            
        dfs(root)    
        postOrder.append(root.val)

        return postOrder

        
        