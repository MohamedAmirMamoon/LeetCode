class Solution:
    def frequencySort(self, s: str) -> str:
        # string sort on decreasing order of freq of chars
        seen = defaultdict(int)
        for c in s:
            seen[c] += 1

        # now we have frequency of strings

        decreasingOrder = sorted(seen.items(), key = lambda x: x[1], reverse = True)

        # now we have decreasing order of elements
        finalString = ""

        for item in decreasingOrder:
            print(item[0])
            while seen[item[0]] != 0:
                finalString += item[0]
                seen[item[0]] -= 1

        return finalString