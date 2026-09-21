class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # array of strs
        # group all of the anagrams together


        # hwo can we group them


        
        map = defaultdict(list)

        for str in strs:
            charMap = 26 * [0]
            # add each strings defaultdcit into map as key, value is gonna be the list of anagrams within that group
            # then return all the values not keys in the map        
            for c in str:
                charMap[ord(c) - ord('a')] += 1
            map[tuple(charMap)].append(str)
            del charMap

        # return our values
        return list(map.values())