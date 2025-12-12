class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort for dependencies

        preMap = {}

        for i in range(numCourses):
            preMap[i] = []
        
        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)

        visited = set()
        done = set() 
        def dfs(crs):
            if crs in done:
                return True
            if crs in visited:
                return False
            if preMap[crs] == []:
                done.add(crs)
                return True
            # 1 -> 3 2
            # 4 -> 2

            
            visited.add(crs)
            for preReq in preMap[crs]:
                if not dfs(preReq):
                    return False
            visited.remove(crs)
            
            done.add(crs)
            return True
                

        for crs, preReq in prerequisites:
            if not dfs(crs):
                return False
        
        return True
