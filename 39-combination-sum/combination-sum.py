class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        finalResult = []
        candidates.sort()


        def backtrack(i, current, total):
            # we choose and we dont choose for each element
            if total == target:
                finalResult.append(current.copy())
                return
            if total > target or i >= len(candidates):
                return

            # we add the integer
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])
            current.pop()

            backtrack(i+1, current, total)
            
            # 2 2 2

        backtrack(0, [], 0)
        return finalResult