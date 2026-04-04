class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # all combinations of well formed parenthesis

        # n pairs of parenthesis
        # this is backtracking with a constraint
        # so we run our algorithm, whne we decide to do either parenthesis
            # it either must be possible for future parenthesis
            # completing prior parenthesis
        # pairs of parenthsis is amount n

        # 



        result = []
        # we go upto 3
        # ((()))
        # ()(())
        # (())()
        
        maxLeft = n
        maxRight = n

        def backtrack(index, path):
            nonlocal maxLeft, maxRight
            temp = path
            if index == n*2:
                print(temp)
                result.append(temp)

            #take this 
            if index != (n*2) - 1 and maxLeft > 0:
                maxLeft -= 1
                path += "("
                backtrack(index+1, path)
                maxLeft += 1
                path = path[:-1]


            if index != 0 and maxRight > 0 and maxRight != maxLeft:
                #take other option
                maxRight -= 1
                path += ")"
                backtrack(index+1, path)
                maxRight += 1
                path = path[:-1]



        backtrack(0, "")
        return result 
        
        