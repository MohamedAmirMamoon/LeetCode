class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # array of binary
        # del one
        # so we left right pointer with just one 0
        # when more than one 0, then we add to left pointer until only one 0 again
   
        left = 0
        longest = 0

        lastZero = -1

        for right in range(len(nums)):
            if nums[right] == 0:
                left = lastZero + 1
                lastZero = right 
            longest = max(longest, right - left)

        return longest