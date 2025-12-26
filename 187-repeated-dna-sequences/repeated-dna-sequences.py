class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Nucelotides, which make up a dna sequence
        # ACGT

        # all 10 letter long sequences, that occur more than once in a s

        # fixed window sizing of 10
        
        # we get the first substr
        # save a snapshot in set
            # add string from index to index to set
        # if this snapshot exists, more than once, add to final output

        # then add 1 to left and right
        dnaMap = defaultdict(int)
        left = 0
        finalOutput = []

        print(len(s))
        
        for right in range(10, len(s)+1):
            stringSnapshot = s[left:right]
            print(stringSnapshot)
            dnaMap[stringSnapshot] += 1

            if dnaMap[stringSnapshot] == 2:
                finalOutput.append(stringSnapshot)
            left += 1

        return finalOutput


            
            

            



        