class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rotate clockwise 90 degrees
        # so how it works is its going to be a perfect square
        # so bottom row going up would go to first item in each array
        # so first row going down wold go to last item

        # create a copy of matrix, 

        arrayAmount = len(matrix[0])
        temp = [row[:] for row in matrix]
        print(temp)
        indexItem = 0
        # each array
        for array in temp:
            # iterating through each item in array
            [4,5,6]
            print(array)
            # [[4, 1, 1],[5, 2, 4],[6, 3, 7]]
            for i in range(arrayAmount):
                matrix[indexItem].insert(0, array[i])
                matrix[indexItem].pop()
                indexItem += 1
            indexItem = 0

     
                


        