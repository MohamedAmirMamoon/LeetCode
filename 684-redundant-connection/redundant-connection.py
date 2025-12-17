class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(len(edges) + 1):
            adj[i] = []
    

        edge = []
        cycleFound = False
        visited = set()
        def dfs(node, par):
            nonlocal cycleFound, edge
    
            if visit[node]:
                return

            visit[node] = True

            for newNode in adj[node]:
                if newNode == par:
                    continue
                if visit[newNode]:
                    # mark 
                    cycleFound = True
                    edge = [newNode, node]
                    return
                dfs(newNode, node)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            visit = [False] * (len(edges)+1)

            dfs(n1, -1)
            if cycleFound:
                return [n1, n2]

        return []