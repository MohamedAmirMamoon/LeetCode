class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        finalResult = []
        candidates.sort()
        # no duplicates

        def backtrack(i, current, total):
            # we choose and we dont choose for each element
                
            if total == target:
                finalResult.append(current.copy())
                return
                    
            if total > target or i >= len(candidates):
                return
            

            # we add the integer
            current.append(candidates[i])
            backtrack(i+1, current, total + candidates[i])
            current.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            backtrack(i+1, current, total)
            
            # 2 2 2

        backtrack(0, [], 0)
        return finalResult