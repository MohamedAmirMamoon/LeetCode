class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substr without duplicates
        
        if s == "":
            return 0
        
        left = 0
        right = 1

        maxSubstr = 1
        chars = set()
        chars.add(s[left])

        # iterate through our string, 
        while right != len(s):

            while s[right] in chars:
                chars.remove(s[left])
                left += 1
         
            maxSubstr = max(maxSubstr, right - left + 1)
            chars.add(s[right])
                
            right += 1

            

        # abcabcbb
        return maxSubstr