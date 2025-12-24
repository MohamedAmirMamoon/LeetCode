class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # longest subsequence 
        # iterate right left
        
        nums.sort()
        print(nums)
        left = 0
        longest = 0
        instance = False

        if nums[-1] == nums[0]:
            return 0

        for right in range(len(nums)):
            diff = nums[right] - nums[left]
            while diff > 1:
                left += 1
                diff = nums[right] - nums[left]
        
            if diff == 1:
                longest = max(longest, abs(right - left + 1))
                        
        return longest

        # 1 3 3 3 6