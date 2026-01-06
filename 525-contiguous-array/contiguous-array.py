class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # we have array of 0's and 1's we want to find the max lenght of ubarray wiht equal 0 and 1

        # we can use prefixSum
        # as we go we keep track of amount of 0's and 1's
        # as we go we add the difference into a map, mapped to an index
        # then as we go, we find the biggest array with that by mapping what we need to remove upto and building array

        zeros = 0
        ones = 0
        seen = {}
        maxCount = 0

        for i, num in enumerate(nums):
            if num == 1:
                ones += 1
            else:
                zeros += 1

            diff = zeros - ones

            # 2-1 = 1
            # 1 -> 0
            if diff not in seen:
                seen[diff] = i
            
            if ones == zeros:
                maxCount = max(ones + zeros, maxCount)
            else:
                indexCut = seen[diff] 
                maxCount = max(i - indexCut, maxCount)
            
            # 1 1 1 0
    
        return maxCount

