class Solution:
    def decodeString(self, s: str) -> str:
        # return the decoded string
        # so the number outside brackets, the encoded item is repeated that many times (k times)
        # never white spaces
        # always well formed

        # if c !=  ]
            # then we add to stack
        # if c == ]
            # then we go back until we reach [
            # on the way
        
        

        # so we add to stack
        # when we see [
            # 3[a
            # 3 * (a + 2 *(c))
        # when we see ]
        # int, ascii, bracket
        stack = []
        for c in s:
            print(''.join(stack))
            print('char: ',c)
            if c != ']':
                stack.append(c)
            else:
                substr = ""

                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                substr = int(k) * substr
                
                stack.append(substr)
                

        return ''.join(stack)

        


            

