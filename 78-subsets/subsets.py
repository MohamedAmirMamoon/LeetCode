class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        finalResult = []
        seen = set()
        

        def backtrack(i, current):
            print("index: ",i)
            print("current: ", current)
            if i >= len(nums):
                finalResult.append(current.copy())
                return
            
            current.append(nums[i])
            print('calling b1')
            backtrack(i+1, current)
            
            current.pop()
            print('calling b2')
            backtrack(i+1, current)
            # 1 2 3
            # 2
            # 1 2
            # 2
            # 1 3
            # 



        backtrack(0, [])

        # 1 2 3
        # 1 
        return finalResult