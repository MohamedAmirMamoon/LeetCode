class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # at last index
        goal = len(nums) - 1



        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False
            
        # start at index
        # stop at index
        # step index


