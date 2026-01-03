class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # return first num rows of pascals triangle
        # start with the first one
        # then we always add two ones to sides
        # you do the bisum of each above

        pTriangle = [[1]]
        for i in range(numRows - 1):
            arr = []
            arr.append(1)
            if i != 0:
                # then we run bisum
                # whats constantly being done
                # now we loop through with pointers
                left = 0
                lastRow = pTriangle[-1]
                for right in range(1, len(lastRow)):
                    arr.append(lastRow[left] + lastRow[right])
                    left += 1
            
            arr.append(1)
            pTriangle.append(arr)

        return pTriangle
