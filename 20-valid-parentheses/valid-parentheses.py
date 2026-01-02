class Solution:
    def isValid(self, s: str) -> bool:
        # how do we use a stack here
        # store all of these in a stack
        # ( [ { } ] )
        # only vaid if
        # ( -> )
        # and has to be done in correct order

        # we append to stack, and we remove and check each time
        pars = {')': '(', ']': '[', '}': '{'}
        stack = deque()

        # so we iterate through the string
        # on each string item, if its in pars and is a closing, the top item in stack should be its associated opening
        # if not then return false
        # if so we continue and remove the element
        # we return true if our stack is empty

        for c in s:
            if c in pars:
                # now we check if last stackelement is associated
                if stack and stack.pop() == pars[c]:
                    continue
                else:
                    return False

            stack.append(c)

        return False if stack else True

