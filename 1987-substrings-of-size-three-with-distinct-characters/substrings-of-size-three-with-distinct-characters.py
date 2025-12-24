class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # no repeated chars
        # reutnr num of good substrs of len 3 in s
        totalgs = 0
       
        for i in range(len(s) - 2):
            window = s[i:i+3]
            if len(set(window)) == 3:
                totalgs += 1



        return totalgs



