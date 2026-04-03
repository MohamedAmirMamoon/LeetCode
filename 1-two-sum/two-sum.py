class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given nums
        # target
        # return two indexes that add up to target
        # each input would have exactly one sol

        # we could just do a nested for loop, would be super inefficient, but we would get our answer
        # may not use same element twice, so no index used twice

        # we can go through the array and as we go, store the index with the item in a map
        # then if we find the compliment of another item existing in this map, we can return the indices of both
        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment], i]

            seen[nums[i]] = i
        



