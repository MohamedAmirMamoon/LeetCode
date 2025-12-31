class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left and right pointer
        # left on the first number
        # right on the second number
        # if left is a 0 and right is not, then we swap
        # 0 1 0 3 12
        # 1 0 0 3 12
        # 1 3 0 0 12
        # 1 3 12 0 0 

        # 1 1 0 2 0 

        left, right = 0, 1

        while right < len(nums):
            
            if nums[left] == 0 and nums[right] != 0:
                temp = nums[right]
                nums[left] = temp
                nums[right] = 0
                left += 1
            
            while nums[left] != 0:
                left += 1
                if left >= len(nums):
                    break
            
            if left >= right:
                right = left + 1
            else:
                right += 1

        return nums
                

        