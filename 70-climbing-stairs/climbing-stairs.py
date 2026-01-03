class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        # n = 5
        # 5 not in memo
        # memo[5] = recurse backwards to 4 and 3
        # n=4 and n=3 not in memo
        # we call it agin at each
        # memo[4] = recurse backwards to 3 and 2, so bc of this we should just do n-2 first
        # memo[3] = recurse backwards to 2 and 1, they exist so memo[3] = 3
        # memo[4] is claled for 3 and 2 memo[4] = 3 + 2 = 5
        # memo[5] = memo[3] + memo[4] = 8

        def recurse(n):
            if n in memo:
                return memo[n]
            else:
                # now we know its not in our table so we can find it
                memo[n] = recurse(n-2) + recurse(n-1)
                return memo[n]

        return recurse(n)