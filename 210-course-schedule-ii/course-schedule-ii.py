class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # course b to take take course a

        # return ordering of courses you should take to finish all
        # if many valid return any
        # return empty if impossible

        # count how many times it is a preReq
        if numCourses == 1:
            return [0]

        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)

        visited = set()
        done = set() 
        order = []

        def dfs(crs):
            if crs in done:
                return True
            if crs in visited:
                return False
            if preMap[crs] == []:
                done.add(crs)
                order.append(crs)
                return True
         
            visited.add(crs)
            for preReq in preMap[crs]:
                if not dfs(preReq):
                    return False
            
            
            visited.remove(crs)
            
            done.add(crs)
            order.append(crs)
            return True
                

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        
        return order
        


        # so we go through each 
        # 0     1       2       3       4
        #       0       0       1,2