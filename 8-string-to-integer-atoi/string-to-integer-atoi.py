class Solution:
    def myAtoi(self, s: str) -> int:
        # no
        tempString = ""
        multiplier = 1
        foundMultiplier = False

        for i in range(len(s)):
            print(i)
            print(s[i])
            if not tempString:
                if foundMultiplier and not s[i].isdigit():
                    return 0
                if s[i] == ' ':
                    continue
                elif s[i] == '-':
                    multiplier *= -1
                    foundMultiplier = True
                    continue
                elif s[i] == '+':
                    foundMultiplier = True
                    continue
                elif not s[i].isdigit():
                    break
            if s[i].isdigit():
                tempString += s[i]
            else:
                break
            

        print(tempString)

        finalInt = 0
        if tempString:
            finalInt = int(tempString)
            finalInt *= multiplier

        bit32Int = 2**31

        if finalInt >= bit32Int:
            finalInt = bit32Int - 1
        elif finalInt < -bit32Int:
            finalInt = -bit32Int 

        return finalInt
        
                

        