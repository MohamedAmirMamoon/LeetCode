class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort for dependencies
        
        courseGraph = {}
        for i in range(numCourses):
            courseGraph[i] = []

        for a, b in prerequisites:
            courseGraph[a].append(b)
            

        # how would we know if we can take all courses
        # we go through graph start with first one
        # must take 1 first before taking 0
        # [0, 1] [0, 3] [3 1] [2, 0]
        # 0: 1 3 
        # 1: 3 4
        # 2: 0
        # 3: 
        # 4: 1, 0

        # we loop through their prereqs
        # on each we check if they have prereqs
        # we mark the prereq as visited
        # then if we see that a visited course is also a prereq for its prereq then we return false
        # otherwise we keep going and should return True
        done = set()
        visited = set()
        def dfs(crs):
            if crs in done:
                return True
            if len(courseGraph[crs]) == 0:
                return True
            if crs in visited:
                return False
        
            visited.add(crs)
            # 0 1 4 
            for preReq in courseGraph[crs]:
                if not dfs(preReq):
                    return False
            
            done.add(crs)

            visited.remove(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True









        '''
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
        '''