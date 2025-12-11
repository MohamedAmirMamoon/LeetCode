class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        visited = set()

        for i in range(numCourses):
            preMap[i] = []

        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)

        # now we have initialized preMap

        def dfs(crs):
            if crs in visited:
                return False # proves it is a cycle
            if len(preMap[crs]) == 0:
                return True

            visited.add(crs)
            # now we go through each prereq
            for preReq in preMap[crs]:
                if not dfs(preReq):
                    return False
            # why this
            visited.remove(crs)

            preMap[crs] = []
            return True

        # now go through all courses, and run dfs on each to see whatever it maps to is correct and does not return false
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True