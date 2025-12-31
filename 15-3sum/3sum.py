class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        
        nums.sort()
        result = []
        seen = set()

        # we use left and right two pointers as well
        
        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1
           

            # -4 -1 -1 0 1 2
            # target should equal 0
            # -1 + -4 + 2
            while left < right:
                    
                if left == i:
                    left += 1
                if right == i:
                    right -= 1
        
                sum = nums[i] + nums[left] + nums[right]
                sumSnapshot = [nums[i], nums[left], nums[right]]
                
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # now we add to result
                    if tuple(sumSnapshot) not in seen:
                        result.append(tuple(sumSnapshot))
                        seen.add(tuple(sumSnapshot))
                    left += 1
                    right -=1
        return result
            
                
            

