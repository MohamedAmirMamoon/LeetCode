class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutations
        # 1 2 3
        # 1 3 2
        # 2 1 3
        res = []
        if len(nums) == 1:
            return [nums.copy()]   # return a list of permutations

        for i in range(len(nums)):
            removed = nums.pop(0)
            
            perms = self.permute(nums)

            for perm in perms:
                perm.append(removed)
                res.append(perm)

            nums.append(removed)

        return res

            

            