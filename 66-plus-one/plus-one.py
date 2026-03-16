class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # each digit is ith digit in array
        # no leading 0's

        # we iterate through the back of the array, 
        #if the number = 9, then we make it 0
        # go to next index repeat
        # 4321 -> 4322
        # 9
        carryExists = True
        index = len(digits) - 1 # this is last digit
        while carryExists:
            carryExists = False
            if digits[index] == 9:
                digits[index] = 0
                carryExists = True
            elif index == 0:
                digits[index] += 1
                break
            else:
                digits[index] += 1

            index -=1 
            if index < 0:
                digits.insert(0, 1)
                carryExists = False
            
        return digits

    


            