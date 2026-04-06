class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # nums has n amount unique binary strings
        # each of them are length n as well
        # return a binary string of length n not appearing in the nums array

        # iterate through we want to get to the final index, while not having an instance of it in nums
        """
        result = []
        numsSet = set()
        for str in nums:
            numsSet.add(str)

        def backtrack(index, path):
            # take 1 or take 0
            if index == len(nums):
                if path not in numsSet:
                    result.append(path)
                return

            # take 0
            backtrack(index + 1, path + '0')

            backtrack(index + 1, path + '1')

        backtrack(0, "")

        return result[0] if result else -1

        """

        # start
        # we iterate through entire nums with index
        # 01 10 
        # 11
        # if there are n strings and all n length
        # we can just take something different from each string at each index
        finalResult = ""
        for i, num in enumerate(nums):
            if num[i] == '0':
                finalResult += '1'
            else:
                finalResult += '0'
            
        return finalResult











