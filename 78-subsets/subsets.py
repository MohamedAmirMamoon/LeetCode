class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
            # 1 2 3
            # 2
            # 1 2
            # 2
            # 1 3
        result = []
            
        def backtracking(index, path):
            if index == len(nums):
                print(path)
                result.append(path[:])
                return
            
            # choice 
            # do we take number or not
            path.append(nums[index])
            print(path)
            backtracking(index + 1, path)
            path.pop()

            backtracking(index + 1, path)

        backtracking(0, [])

        # 1 2 3
        # backtrack
        # 1 2
        # backtrack
        # 1 3
        # backtrack
        # 1
        # 2 3
        # 2
        return result