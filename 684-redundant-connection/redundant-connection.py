class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = []
        for i in range(len(edges) + 1):
            parent.append(i)

        def findRoot(node):
            nonlocal parent
            if parent[node] != node:
                return findRoot(parent[node])
            return parent[node] 

        def union(edge1, edge2):
            nonlocal parent
            
            root1 = findRoot(edge1)
            root2 = findRoot(edge2)
            if root1 == root2:
                return [edge1, edge2]
    
            
            parent[root2] = root1

            return []

        for u, v in edges:
            edge = union(u, v)
            if edge != []:
                return edge
        
        # Input: edges = [[1,2],[1,3],[3,4],[2,4]]
        # if parent of 4 is 1, and 3 is 3
        # visited = 1, 2, 4, 3
        # Output: [2,4]
        return []