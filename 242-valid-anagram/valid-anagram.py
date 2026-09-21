class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two strings
        # if both anagrams of eachother return True
        # if not False

        # same amount for each specific char
# done
        # iterate through one add to hashMap with value
        # as we iterate through second remove each char from map 
        # by end if map empty return True
        # otherwise return False

        # basecase: strings diff len, return False

        if len(s) != len(t):
            return False


        charMap = defaultdict(int)
        
        for c in s:
            charMap[c] += 1

        for c in t:
            charMap[c] -= 1
            if charMap[c] == 0:
                del charMap[c]
        
        print(charMap)
        if not charMap:
            return True

        return False