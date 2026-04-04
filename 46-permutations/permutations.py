class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutations
        # 1 2 3
        # 1 3 2
        # 2 1 3
        result = []
        n = len(nums)
        
        def backtrack(index, path):
            if index == n:
                print(path)
                result.append(path[:])
                return 
            
            for num in nums[:]:
                path.append(num)
                removedNum = num
                nums.remove(num) 
                backtrack(index+1, path)
                nums.append(removedNum)
                path.pop()
            
        backtrack(0, [])

        return result

            

            