class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # return max continguous avg value array for len k

        # we need it to be k len
        if len(nums) < k:
            return 0

        sum = 0.0
        for i in range(k):
            sum += nums[i]
        
        maxSum = sum
      
        for i in range(k, len(nums)):
            
           sum += nums[i] - nums[i-k]
           print(nums[i])
           print('subtracted ', nums[i-k])

           maxSum = max(sum, maxSum)

            

        return maxSum/k